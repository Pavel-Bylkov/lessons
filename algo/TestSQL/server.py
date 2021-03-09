# -*- coding: utf-8 -*-
''' Программа для проблематизации сессий: подключаемся к БД,
показываем по одной строке таблицы по очереди, но работа нескольких клиентов одновременно нарушают очередность'''
from flask import Flask, redirect, url_for
from flask import session
from create_db import get_question_after


def index():
    max_quiz = 3
    #quiz = randint(1, max_quiz)
    if 'quiz' in session and session['quiz'] < max_quiz:
        session['quiz'] += 1
    else:
        session['quiz'] = 1
        session['last_question'] = 0
    return '<h1><a href="/test">Тест</a></h1>'

def test():
   result = get_question_after(session['last_question'], session['quiz'])
   if result is None or len(result) == 0:
       return redirect(url_for('result'))
   else:
       session['last_question'] = result[0]
       return '<h1>' + str(session['quiz']) + '<br>' + str(result) + '</h1>'

def result():
   return "<h1>that's all folks!</h1>"


# Создаём объект веб-приложения:
app = Flask(__name__)  
app.config['SECRET_KEY'] = 'VeryStrongKey'
app.add_url_rule('/', 'index', index)   # создаёт правило для URL '/'
app.add_url_rule('/test', 'test', test) # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result) # создаёт правило для URL '/test'

if __name__ == "__main__":
   # Запускаем веб-сервер:
   app.run()
