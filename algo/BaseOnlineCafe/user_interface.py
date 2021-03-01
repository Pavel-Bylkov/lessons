from base_dish import Dish, Menu, Receipt


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
            add_menu(all_menu)
        elif question == "2":
            print_all_menu(all_menu)
        elif question == "3":
            edit_menu(all_menu, all_dishes)
        elif question == "4":
            del_menu(all_menu)
        elif question == "5":
            add_dish(all_dishes)
        elif question == "6":
            print_all_dishes(all_dishes)
        elif question == "7":
            edit_dish(all_dishes)
        elif question == "8":
            del_dish(all_dishes)
        elif question != "0":
            print("Выбор не распознан.Попробуйте ещё раз ...")
        else:
            run = False