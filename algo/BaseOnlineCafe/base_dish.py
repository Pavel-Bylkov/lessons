class Dish:
    def set_dish_info(self, name_dish: str, weight: str, price: str) -> None:
        self.name_dish = name_dish
        self.weight = weight
        self.price = price
    def get_dish_info(self) -> str:
        return f"{self.name_dish} ({self.weight} гр.) - {self.price} руб."
    def edit(self) -> None:
        run = True
        while run:
            print('''Режим редактирования блюда {}:
            Вам доступны следующие действия:
            1 - Изменить название
            2 - Изменить вес
            3 - Изменить цену
            0 - Выйти из режима редактирования
            Чтобы сделать какое либо действие, введите соответствующие цифры.
            '''.format(self.name_dish))
            question = input("Что вы желаете сделать?")
            if question == "1":
                self.name_dish = input("Введите название блюда: ")
            elif question == "2":
                self.weight = input("Введите вес порции в граммах (только цифру): ")
            elif question == '3':
                self.price = input("Введите цену за 1 порцию в рублях (только цифру): ")
            elif question == "0":
                run = False
            else:
                print("Выбор не распознан.Попробуйте ещё раз ...")

class Menu:
    def __init__(self, menu_name: str) -> None:
        self.menu_name = menu_name
        self.list_dishes = []
    def add_dish(self, dish: Dish) -> None:
        if dish not in self.list_dishes:
            self.list_dishes.append(dish)
    def print_menu(self) -> None:
        print(f"Меню : {self.menu_name}")
        print("Список блюд:")
        n = 1
        for dish in self.list_dishes:
            print(n, "-", dish.get_dish_info())
            n += 1 
    def edit(self) -> None:
        run = True
        while run:
            print('''Режим редактирования меню {}:
            Вам доступны следующие действия:
            1 - Изменить название
            2 - Вывести список блюд
            3 - Удалить блюдо
            0 - Выйти из режима редактирования
            Чтобы сделать какое либо действие, введите соответствующие цифры.
            '''.format(self.menu_name))
            question = input("Что вы желаете сделать?")
            if question == "1":
                menu_name = input("Введите названию меню")
                self.menu_name = menu_name
            elif question == "2":
                if self.list_dishes:
                    n = 1
                    for dish in self.list_dishes:
                        print(n, "-", dish.get_dish_info())
                        n += 1
                else:
                    print("Список блюд пуст.")
            elif question == '3':
                number = int(input("Введите номер блюда для удаления (0 - вернуться назад):"))
                if number != 0 and 1 <= number <= len(self.list_dishes):
                    dish = self.list_dishes.pop(number - 1)
                    print(dish.get_dish_info(), "удалено из меню")
            elif question == "0":
                run = False
            else:
                print("Выбор не распознан.Попробуйте ещё раз ...")

class Receipt:
    def __init__(self, name_client: str) -> None:
        from datetime import datetime as dt
        self.datetime = dt.now()
        self.name_client = name_client
        self.result_price = 0
        self.order = {}
    def add_dish(self, menu_name: str, dish: Dish) -> None:
        if menu_name in self.order:
            self.order[menu_name].append(dish)
        else:
            self.order[menu_name] = [dish]
        self.result_price += int(dish.price)
    def print_receipt(self) -> None:
        print(f"Заказ от {self.name_client}:")
        print(self.datetime.strftime("%d-%m-%Y %H:%M"))
        n = 1
        for menu_name in self.order:
            print("Из меню:", menu_name)
            for dish in self.order[menu_name]:
                print(n, dish.get_dish_info())
                n += 1 
        print("Итого цена заказа:", self.result_price, "руб.")
