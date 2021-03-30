import os
from flask import Flask, session, request, redirect, url_for, render_template
from db_scripts import get_question_after, get_quises

def start_quis(quiz_id):
    '''создаёт нужные значения в словаре session'''
    session['quiz'] = quiz_id
    session['last_question'] = 0

def end_quiz():
    session.clear()

def quiz_form():
    ''' функция получает список викторин из базы и формирует форму с выпадающим списком'''
    q_list = get_quises()
    return render_template('first.html', q_list=q_list)

def index():
    ''' Первая страница: если пришли запросом GET, то выбрать викторину, 
    если POST - то запомнить id викторины и отправлять на вопросы'''
    if request.method == 'GET':
        # викторина не выбрана, сбрасываем id викторины и показываем форму выбора
        start_quis(-1)
        return quiz_form()
    else:
        # получили дополнительные данные в запросе! Используем их:
        quest_id = request.form.get('quiz') # выбранный номер викторины 
        start_quis(quest_id)
        return redirect(url_for('test'))

def test():
    '''возвращает страницу вопроса'''
    # что если пользователь без выбора викторины пошел сразу на адрес '/test'? 
    if not ('quiz' in session) or int(session['quiz']) < 0:
        return redirect(url_for('index'))
    else:
        # тут пока старая версия функции:
        result = get_question_after(session['last_question'], session['quiz'])
        if result is None or len(result) == 0:
            return redirect(url_for('result'))
        else:
            session['last_question'] = result[0]
            # если мы научили базу возвращать Row или dict, то надо писать не result[0], а result['id']
            return '<h1>' + str(session['quiz']) + '<br>' + str(result) + '</h1>'

def result():
    end_quiz()
    return "that's all folks!"

folder = os.getcwd() # запомнили текущую рабочую папку
# Создаём объект веб-приложения:
app = Flask(__name__, template_folder=folder, static_folder=folder) # первый параметр - имя модуля
                            # параметр с именем static_folder определяет имя папки, содержащей статичные файлы
                            # параметр с именем template_folder определяет имя папки, содержащей шаблоны

app.add_url_rule('/', 'index', index, methods=['post', 'get'])   # создаёт правило для URL '/'
app.add_url_rule('/test', 'test', test) # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result) # создаёт правило для URL '/test'
# Устанавливаем ключ шифрования:
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run()
