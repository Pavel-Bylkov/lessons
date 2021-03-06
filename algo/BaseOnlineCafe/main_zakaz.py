from time import sleep
from admin_interface import admin
from user_interface import user

all_dishes = {}
all_menu = {} 
right_login = "Natalia" 
right_password = "12345"
run = True
while run:
    print('''
    Программа для "Онлайн-заказа еды".
    В ней доступны следующие действия:
    1 - Войти в режим администратора
    2 - Сделать заказ
    0 - Закончить выполнение программы
    Чтобы сделать какое либо действие, введите соответствующие цифры.
    ''')
    question = input("Что вы желаете сделать?")
    if question == "1":
        login = input("Введите логин")
        password = input("Введите пароль:")
        if login == right_login and password == right_password:
            admin(all_dishes, all_menu)
        else:
            print("Введен неверный логин или пароль.")
    elif question == "2":
        user(all_menu)
    elif question != "0":
        print("Выбор не распознан.Попробуйте ещё раз ...")
    else:
        run = False
    sleep(2)

"""
Меню "Летнее"
Картофель запеченый	 300 гр - 30 руб
Борщ 200 гр - 25 руб
Компот 150 гр - 10 руб

Меню "Зимнее"
Окрошка 200 гр - 25 руб
Морс 150 гр - 11 руб

Меню "Завтраки"
Омлет - 100 гр - 15 руб
Хлеб 5 гр - 2 руб

Меню "Ужины"

Меню "Бизнес-ланчи"
"""