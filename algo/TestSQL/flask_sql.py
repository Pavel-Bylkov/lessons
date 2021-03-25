from flask import Flask, url_for, redirect
import sqlite3

def index():
    # Устанавливаем соединение с базой данных и отправляем запрос
    conn = sqlite3.connect("Artistc.db")
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM artists WHERE "Birth Year" = (?)', [year])
    data = cursor.fetchall()
 
    # При обработке запроса рассмотрим несколько вариантов:
    # Вариант 1 - в базе нет данных о художниках, родившихся в указанный год
    if len(data) == 0:
        return f'В базе нет данных о художниках, родившихся в {year} году'
    # Вариант 2 - художник, родившийся в указанный год, только один
    elif len(data) == 1:
        return f'В {year} году родился (родилась) {data[0][0]}'
    # Вариант 3 - художников, родившихся в указанный год, несколько
    else:
        result = f'<h3>Список художников, родившихся в {year} году:</h3><ol>'
        for person in data:
            result += '<li>' + person[0] + '</li>'
        result += '</ol>'
    return result

# Запрашиваемый год рождения будем хранить в глобальной переменной
year = int(input('Введите год рождения художника: '))        
app = Flask(__name__)
app.add_url_rule('/', 'index', index)   
 
if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run()
