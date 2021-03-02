from base_dish import Dish, Menu, Receipt

def add_dish(menu, all_dishes):
    number_dish = input("Введите номер блюда ")
    if number_dish in all_dishes:
        menu.add_dish(all_dishes[number_dish])
    else:
        print("неверный номер блюда")

def add_menu(all_menu, all_dishes):
    """Создать новое меню (добавить)"""
    menu_name = input("Введите названию меню")
    number_menu = str(len(all_menu) + 1)
    all_menu[number_menu] = Menu(menu_name) 
    run = True
    while run:
        print('''Режим добавление блюд
        Вам доступны следующие действия:
        1 - Добавить блюдо
        2 - Вывести список блюд
        0 - Выйти из режима добавление
        Чтобы сделать какое либо действие, введите соответствующие цифры.
        ''')
        question = input("Что вы желаете сделать?")
        if question == "1":
            add_dish(all_menu[number_menu], all_dishes)
        elif question == "2":
            print_all_dishes(all_dishes)
        elif question != "0":
            print("Выбор не распознан.Попробуйте ещё раз ...")
        else:
            run = False

def print_all_menu(all_menu):
    """Вывести содержимое меню"""
    if all_menu:
        print("""Список доступных меню:""")
        for n in all_menu:
            print(n, "-", all_menu[n].menu_name)
        run = True
        while run:
            print('''Введите номер меню, для просмотра
            0 - Вернуться назад в Режим Админа
            Чтобы сделать какое либо действие, введите соответствующие цифры.
            ''')
            question = input("Что вы желаете сделать?")
            if question == "0":
                run = False
            elif question in all_menu:
                all_menu[question].print_menu()
            else:
                print("Выбор не распознан.Попробуйте ещё раз ...")
    else:
        print("Список меню пуст.")

def edit_menu(all_menu, all_dishes):
    """Редактировать меню"""
    if all_menu:
        print("""Список доступных меню:""")
        for n in all_menu:
            print(n, "-", all_menu[n].menu_name)
        print('''Введите номер меню, для редактирования
        0 - Вернуться назад в Режим Админа
        Чтобы сделать какое либо действие, введите соответствующие цифры.
        ''')
        question = input("Что вы желаете сделать?")
        if question == "0":
            run = False
        elif question in all_menu:
            run = True
            while run:
                print('''Режим редактирования меню {}:
                Вам доступны следующие действия:
                1 - Изменить название
                2 - Вывести список блюд
                3 - Удалить блюдо
                4 - Добавить блюдо
                0 - Выйти из режима редактирования
                Чтобы сделать какое либо действие, введите соответствующие цифры.
                '''.format(self.menu_name))
                question2 = input("Что вы желаете сделать?")
                if question2 == "1":
                    all_menu[question].edit_name()
                elif question2 == "2":
                    all_menu[question].print_menu()
                elif question2 == '3':
                    number = int(input("""Введите номер блюда для удаления 
                    (0 - вернуться назад): """))
                    all_menu[question].del_dish(number)
                elif question2 == '4':
                    add_dish(all_menu[question], all_dishes)
                elif question == "0":
                    run = False
                else:
                    print("Выбор не распознан.Попробуйте ещё раз ...")
    else:
        print("Список меню пуст.")

def del_menu(all_menu):
    """Удалить меню"""
    if all_menu:
        print("""Список доступных меню:""")
        for n in all_menu:
            print(n, "-", all_menu[n].menu_name)
        run = True
        while run:
            print('''Введите номер меню, для удаления
            0 - Вернуться назад в Режим Админа
            Чтобы сделать какое либо действие, введите соответствующие цифры.
            ''')
            question = input("Что вы желаете сделать?")
            if question == "0":
                run = False
            elif question in all_menu:
                del all_menu[question]
                if int(question) <= len(all_menu):
                    for n in range(int(question), len(all_menu) + 1):
                        all_menu[str(n)] = all_menu[str(n + 1)]
                    del all_menu[str(n + 1)]
            else:
                print("Выбор не распознан.Попробуйте ещё раз ...")
    else:
        print("Список меню пуст.")

def add_dish(all_dishes):
    """Добавить блюдо в список блюд"""
    number_dish = str(len(all_dishes) + 1)
    all_dishes[number_dish] = Dish()
    name_dish = input("Введите название блюда: ")
    weight = input("Введите вес порции в граммах (только цифру): ")
    price = input("Введите цену за 1 порцию в рублях (только цифру): ")
    all_dishes[number_dish].set_dish_info(name_dish, weight, price) 

def print_all_dishes(all_dishes):
    """Добавить блюдо в список блюд"""
    if all_dishes:
        print("""Список доступных блюд:""")
        for n in all_dishes:
            print(n, "-", all_dishes[n].get_dish_info())
    else:
        print("Список блюд пуст.")

def edit_dish(all_dishes):
    """Редактировать блюдо"""
    if all_dishes:
        print("""Список доступных блюд:""")
        for n in all_dishes:
            print(n, "-", all_dishes[n].get_dish_info())
        run = True
        while run:
            print('''Введите номер блюда, для редактирования
            0 - Вернуться назад в Режим Админа
            Чтобы сделать какое либо действие, введите соответствующие цифры.
            ''')
            question = input("Что вы желаете сделать?")
            if question == "0":
                run = False
            elif question in all_dishes:
                print("Редактируется блюдо:", all_dishes[question].get_dish_info(),
                '''
                Вам доступны следующие действия:
                1 - Изменить название
                2 - Изменить вес
                3 - Изменить цену
                0 - Выйти из режима редактирования
                Чтобы сделать какое либо действие, введите соответствующие цифры.
                ''')
                question2 = input("Что вы желаете сделать?")
                if question2 == "1":
                    all_dishes[question].edit_name()
                elif question2 == "2":
                    all_dishes[question].edit_weight()
                elif question2 == '3':
                    all_dishes[question].edit_price()
            else:
                print("Выбор не распознан.Попробуйте ещё раз ...")
    else:
        print("Список блюд пуст.")

def del_dish(all_dishes):
    """Удалить блюдо"""
    if all_dishes:
        print("""Список доступных блюд:""")
        for n in all_dishes:
            print(n, "-", all_dishes[n].get_dish_info())
        run = True
        while run:
            print('''Введите номер блюда, для удаления
            0 - Вернуться назад в Режим Админа
            Чтобы сделать какое либо действие, введите соответствующие цифры.
            ''')
            question = input("Что вы желаете сделать?")
            if question == "0":
                run = False
            elif question in all_dishes:
                del all_dishes[question]
                if int(question) <= len(all_dishes):
                    for n in range(int(question), len(all_dishes) + 1):
                        all_dishes[str(n)] = all_dishes[str(n + 1)]
                    del all_dishes[str(n + 1)]
            else:
                print("Выбор не распознан.Попробуйте ещё раз ...")
    else:
        print("Список блюд пуст.")

def admin(all_dishes, all_menu):
    """Режим администратора для "Онлайн-заказа еды"."""
    run = True
    while run:
        print('''
        Режим администратора для "Онлайн-заказа еды".
        В ней доступны следующие действия:
        1 - Создать новое меню (добавить)
        2 - Вывести содержимое меню
        3 - Редактировать меню
        4 - Удалить меню
        5 - Добавить блюдо в список блюд
        6 - Распечатать весь список блюд
        7 - Редактировать блюдо
        8 - Удалить блюдо
        0 - Выйти из режима администратора
        Чтобы сделать какое либо действие, введите соответствующие цифры.
        ''')
        question = input("Что вы желаете сделать?")
        if question == "1":
            add_menu(all_menu, all_dishes)
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