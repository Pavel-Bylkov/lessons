import sqlite3
db_name = 'quiz.sqlite'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
    except Error as e:
        print(e)

def do(string):
    cursor.execute(string)
    conn.commit()

def close():
    conn.commit()
    cursor.close()
    conn.close()

def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
 
    do('''CREATE TABLE IF NOT EXISTS quiz (
           id INTEGER PRIMARY KEY,
           name VARCHAR,
           age_from INTEGER,
           age_to INTEGER)''')
 
    do('''CREATE TABLE IF NOT EXISTS question (
               id INTEGER PRIMARY KEY,
               question VARCHAR,
               answer VARCHAR,
               wrong1 VARCHAR,
               wrong2 VARCHAR,
               wrong3 VARCHAR)''')
 
    do('''CREATE TABLE IF NOT EXISTS quiz_content (
               id INTEGER PRIMARY KEY,
               quiz_id INTEGER,
               question_id INTEGER,
               FOREIGN KEY (quiz_id) REFERENCES quiz (id),
               FOREIGN KEY (question_id) REFERENCES question (id) )''')
    close()

def add_questions():
    questions = [
        ('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два'),
        ('Каким станет зелёный утёс, если упадёт в Красное море?', 'Мокрым', 'Красным',
        'Не изменится', 'Фиолетовым'),
        ('Какой рукой лучше размешивать чай?', 'Ложкой', 'Правой', 'Левой', 'Любой'),
        ('Что не имеет длины, глубины, ширины, высоты, а можно измерить?', 'Время', 
        'Глупость', 'Море', 'Воздух'),
        ('Когда сетью можно вытянуть воду?', 'Когда вода замёрзла', 'Когда нет рыбы', 
        'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
        ('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Парашют', 'Облако')
    ]
    open()
    cursor.executemany('''INSERT INTO question (question, answer, wrong1, wrong2, wrong3)
             VALUES (?,?,?,?,?)''', questions)
    close()

def add_quiz():
    quizes = [
        ('Своя игра', 5, 10),
        ('Кто хочет стать миллионером?', 8, 12),
        ('Самый умный', 12, 18)
    ]
    open()
    cursor.executemany('''INSERT INTO quiz (name,  age_from,  age_to) VALUES (?, ?, ?)''', quizes)
    close()
 
def add_links():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"
    conf_tabl = [[1, 1],  [1, 3], [1, 5], [1, 6],
                [2, 2], [2, 4],
                [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6]]
    for conf in conf_tabl:
        cursor.execute(query, conf)
        conn.commit()
    """answer = input("Добавить связь (y / n)?")
    while answer != 'n':
        quiz_id = int(input("id викторины: "))
        question_id = int(input("id вопроса: "))
        cursor.execute(query, [quiz_id, question_id])
        conn.commit()
        answer = input("Добавить связь (y / n)?")"""
    close()

def clear_db():
    ''' удаляет все таблицы '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()

def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')

def get_question_after(question_id = 0, quiz_id=1):
    ''' возвращает следующий вопрос после вопроса с переданным id
    для первого вопроса передаётся значение по умолчанию '''
    open()
    query = '''
    SELECT quiz_content.id, question.question, question.answer, question.wrong1, question.wrong2, question.wrong3
    FROM question, quiz_content
    WHERE quiz_content.question_id == question.id
    AND quiz_content.id > ? AND quiz_content.quiz_id == ?
    ORDER BY quiz_content.id '''
    cursor.execute(query, [question_id, quiz_id] )
    result = cursor.fetchone()
    close()
    return result

def main():
    clear_db()
    create()
    add_questions()
    add_quiz()
    add_links()
    show_tables()
    # Вывод в консоль вопроса с id=3, id викторины = 1
    print(get_question_after(3, 1))

if __name__ == "__main__":
    main()
