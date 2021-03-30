""" Файл index.html находится, поскольку указана папка шаблонов """

from flask import Flask, render_template
import os

def index():
    """ функция обрабатывает шаблон index.html и возвращает получившийся документ"""
    return render_template('index.html')

folder = os.getcwd() # запомнили текущую рабочую папку
# Создаём объект веб-приложения:
app = Flask(__name__, template_folder=folder, static_folder=folder) # первый параметр - имя модуля
                            # параметр с именем static_folder определяет имя папки, содержащей статичные файлы
                            # параметр с именем template_folder определяет имя папки, содержащей шаблоны

# создаём правило для URL '/': 
app.add_url_rule('/', 'index', index)

# Запускаем веб-сервер:
app.run()
