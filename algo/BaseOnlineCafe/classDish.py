class Dish():
    def set_dish_information(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.dish = f"{self.name} ({self.quantity}гр.) - {self.price} руб."
    def get_dish_information(self):
        return self.dish

class Menu:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_dish(self, dish):
        if dish not in self.products:
            self.products.append(dish)
    
    def menu_output(self):
        print(self.name)
        n = 1
        for dish in self.products:
            print(f"{n}.{dish.name}({dish.quantity}гр.) - {dish.price} руб.")
            n += 1

class Receipt():
    result = 0
    def __init__(self, name):
        self.name = name
        self.order = []
    def set_order(self, parametr1, parametr2):
        self.parametr1 = parametr1
        self.order.append(self.parametr1)
        self.parametr2 = parametr2
        self.result = self.result + int(self.parametr2)
    def get_order(self):
        print("Общий чек: ")
        return self.order
    def get_result(self):
        print("Итого: ")
        return self.result

def menu_entry(menu):
    n_dishes = int(input("Сколько блюд вы желаете добавить (введите цифру)?  "))
    for i in range(n_dishes):
        name = input(f"Введите название {i + 1}-го блюда: ")
        quantity = input("Введите размер порции (только цифру): ")
        price = input("Введите цену за 1 порцию в рублях (только цифру): ")
        d = Dish()
        d.set_dish_information(name, quantity, price)
        menu.add_dish(d)

def order_entry():
    question5 = input("Из какого меню? ")
    if question5 == "11":
        name_menu = br
    if question5 == "22":
        name_menu = din
    if question5 == "33":
        name_menu = bs
    n_order = int(input("Сколько блюд вы желаете заказать (введите цифру)? "))
    for i in range(n_order):
        number = int(input(f"Введите номер {i + 1}-го блюда: "))
        if 1 <= number <= len(name_menu.products):
            check.set_order(name_menu.products[number - 1], name_menu.products[number - 1].price)
        else:
            print(number, "- отстуствует в списке блюд.")
    check.get_order()
    for i in check.order:
        print(f"{i.name}({i.quantity}гр.) - {i.price} руб.")
    check.get_result()
    print(str(check.result) + "руб.")

def interface():
    print('''
    Это программа для "Онлайн-заказа еды".
    В ней доступны следующие действия:
    1 - Заполнить меню
    2 - Вывести меню
    3 - Сделать заказ
    4 - Показать еще раз справку по командам
    0 - Закончить выполнение программы
    Виды меню:
    11 - Завтраки
    22 - Ужины
    33 - Бизнес-ланчи
    Чтобы сделать какое либо действие, введите соответствующие цифры.
    ''')

br = Menu("Завтраки")
din = Menu("Ужины")
bs = Menu("Бизнес-ланчи")
check = Receipt("Сделать заказ")

interface()
question = input("Что вы желаете сделать?")
while question != "0":
    if question == "1":
        question2 = input("Какое меню хотите заполнить?")
        if question2 == "11":
            menu_entry(br)
        if question2 == "22":
            menu_entry(din)
        if question2 == "33":
            menu_entry(bs)
    if question == "2":
        question3 = input("Какое меню хотите вывести? ")
        if question3 == "11":
            br.menu_output()
        if question3 == "22":
            din.menu_output()
        if question3 == "33":
            bs.menu_output()
    if question == "3":
        order_entry()
    if question == "4":
        interface()
    question = input("Что вы желаете сделать?")