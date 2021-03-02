# -*- coding: utf-8 -*-
''' Программа для проблематизации сессий: подключаемся к БД,
показываем по одной строке таблицы по очереди, но работа нескольких клиентов одновременно нарушают очередность'''
from random import randint
from flask import Flask, redirect, url_for
from create_db import get_question_after

quiz = 0
last_question = 0

def index():
    global quiz, last_question
    max_quiz = 3
    #quiz = randint(1, max_quiz)
    if quiz < max_quiz:
        quiz += 1
    else:
        quiz = 1
        last_question = 0
    return '<h1><a href="/test">Тест</a></h1>'

def test():
   global last_question
   result = get_question_after(last_question, quiz)
   if result is None or len(result) == 0:
       return redirect(url_for('result'))
   else:
       last_question = result[0]
       return '<h1>' + str(quiz) + '<br>' + str(result) + '</h1>'

def result():
   return "<h1>that's all folks!</h1>"


# Создаём объект веб-приложения:
app = Flask(__name__)  

app.add_url_rule('/', 'index', index)   # создаёт правило для URL '/'
app.add_url_rule('/test', 'test', test) # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result) # создаёт правило для URL '/test'

if __name__ == "__main__":
   # Запускаем веб-сервер:
   app.run()
