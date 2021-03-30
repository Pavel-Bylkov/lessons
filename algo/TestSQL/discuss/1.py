""" Программа использует flask и запускает веб-сервер. 
При запросе к этому серверу он возвращает содержимое файла index.html
Файл обрабатывается как шаблон. Он не находится! """
from flask import Flask, render_template

def index():
    """ функция обрабатывает шаблон index.html и возвращает получившийся документ"""
    return render_template('index.html')

app = Flask(__name__) 

# создаём правило для URL '/': 
app.add_url_rule('/', 'index', index)

# Запускаем веб-сервер:
app.run()
