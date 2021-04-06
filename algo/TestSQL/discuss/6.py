""" В шаблоне index3.html использовано управление: 
операторы if/else/endif """
from flask import Flask, render_template
import os

def index():
    """ функция обрабатывает шаблон и возвращает получившийся документ"""
    # return render_template('index3.html', header="ЭТО ЗАГОЛОВОК", text="Это текст")
    return render_template('index3.html', text="Это текст")

folder = os.getcwd() + os.sep + "discuss"   # запомнили текущую рабочую папку
# Создаём объект веб-приложения:
app = Flask(__name__, template_folder=folder, static_folder=folder) # первый параметр - имя модуля
                            # параметр с именем static_folder определяет имя папки, содержащей статичные файлы
                            # параметр с именем template_folder определяет имя папки, содержащей шаблоны

# создаём правило для URL '/': 
app.add_url_rule('/', 'index', index)

if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run()
