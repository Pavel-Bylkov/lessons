from admin_interface import del_dish
from base_dish import Dish, Menu, Receipt

def print_all_menu(all_menu):
    """Вывести содержимое меню"""
    if all_menu:
        print("""Список доступных меню:""")
        for n in all_menu:
            print(n, "-", all_menu[n].menu_name)
    else:
        print("Список меню пуст.")

def order_entry(receipt, all_menu):
    run = True
    while run:
        print_all_menu(all_menu)
        print('''Введите номер меню, для выбора бюлюда
            0 - Вернуться назад
            Чтобы сделать какое либо действие, введите соответствующие цифры.
            ''')
        question = input("Что вы желаете сделать?")
        if question in all_menu:
            all_menu[question].print_menu()
            # ToDo Реализовать заполнение заказа блюдами из меню
        elif question == "0":
            run = False
        else:
            print("Выбор не распознан.Попробуйте ещё раз ...")

def user(all_menu):
    """Сделать заказ"""
    name_client = input("Введите ваше имя:")
    receipt = Receipt(name_client)
    run = True
    while run:
        print('''Режим Заказа для "Онлайн-заказа еды".
        В ней доступны следующие действия:
        1 - Выбрать блюдо
        2 - Посмотреть содержимое заказа
        3 - Удалить блюдо
        0 - Завершить заказ
        Чтобы сделать какое либо действие, введите соответствующие цифры.
        ''')
        question = input("Что вы желаете сделать?")
        if question == "1":
            order_entry(receipt, all_menu)
        elif question == "2":
            receipt.print_receipt()
        elif question == "3":
            del_n = int(input("Введите номер блюда, для удаления: "))
            receipt.del_dish(del_n)
        elif question != "0":
            print("Выбор не распознан.Попробуйте ещё раз ...")
        else:
            receipt.print_receipt()
            run = False