class Dish:
    def set_dish_info(self, name: str, quantity: str, price: str) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price
    def get_dish_info(self) -> str:
        return f"{self.name} ({self.quantity}гр.) - {self.price} руб."
class Menu:
    def __init__(self, name: str) -> None:
        self.name = name
        self.products = []
    def add_dish(self, dish: Dish) -> None:
        if dish not in self.products:
            self.products.append(dish)
    def menu_output(self) -> None:
        print(self.name)
        n = 1
        for dish in self.products:
            print(n, '-', dish.get_dish_info())
            n += 1
class Receipt:
    result = 0
    def __init__(self, name: str) -> None:
        self.name = name
        self.order = []
    def set_order(self, dish: Dish) -> None:
        self.order.append(dish.get_dish_info())
        self.result = self.result + int(dish.price)
    def print_order(self) -> None:
        print("Общий чек: ")
        for dish in self.order:
            print(dish)
        print("Итого: ", self.result)

br = Menu("Завтраки")
din = Menu("Ужины")
bs = Menu("Бизнес-ланчи")
check = Receipt("Сделать заказ")

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

def select_menu():
    question2 = input("Какое меню хотите выбрать?")
    if question2 == "11":
        return br
    if question2 == "22":
        return din
    if question2 == "33":
        return bs
    return None

def create_dish():
    name = input(f"Введите название блюда: ")
    quantity = input("Введите размер порции (только цифру): ")
    price = input("Введите цену за 1 порцию в рублях (только цифру): ")
    dish = Dish()
    dish.set_dish_info(name, quantity, price)
    return dish

def entry_menu():
    menu = select_menu()
    if menu:
        while input("Добавить блюдо (да/нет)?") == 'да':
            dish = create_dish()
            menu.add_dish(dish)
    else:
        print("Меню не распознано.") 

def print_menu():
    menu = select_menu()
    if menu:
        menu.menu_output()
    else:
        print("Меню не распознано.") 
def select_dish(menu):
    number = int(input(f"Введите номер блюда: "))
    if 1 <= number <= len(menu.products):
        return menu.products[number - 1]
    else:
        print(number, "- отстуствует в списке блюд данного меню.")
    return None

def order_entry():
    menu = select_menu()
    if menu:
        while input("Добавить блюдо в заказ (да/нет)?") == 'да':
            dish = select_dish(menu)
            if dish:
                check.set_order(dish)
        check.print_order()
    else:
        print("Меню не распознано.") 

interface()
question = input("Что вы желаете сделать?")
while question != "0":
    if question == "1":
        entry_menu()
    elif question == "2":
        print_menu()
    elif question == "3":
        order_entry()
    elif question == "4":
        interface()
    else:
        print("Выбор не распознан. Попробуйте еще раз.")
    question = input("Что вы желаете сделать?")