# начало урока База данных 
class Dish:
    def set_dish_info(self, name_dish, weight, price):
        self.name_dish = name_dish
        self.weight = weight
        self.price = price
    def get_dish_info(self):
        return f"{self.name_dish} ({self.weight} гр.) - {self.price} руб."

class Menu:
    def __init__(self, menu_name):
        self.menu_name = menu_name
        self.list_dishes = []
    def add_dish(self, dish):
        if dish not in self.list_dishes:
            self.list_dishes.append(dish)
    def print_menu(self):
        print(f"Меню : {self.menu_name}")
        print("Список блюд:")
        n = 1
        for dish in self.list_dishes:
            print(n, dish.get_dish_info())
            n += 1 

class Receipt:
    def __init__(self, name_order):
        self.name_order = name_order
        self.result_price = 0
        self.order = {}
    def add_dish(self, menu_name, dish):
        if menu_name in self.order:
            self.order[menu_name].append(dish)
        else:
            self.order[menu_name] = [dish]
        self.result_price += int(dish.price)
    def print_receipt(self):
        print(f"Заказано {self.name_order}:")
        n = 1
        for menu_name in self.order:
            print("Из меню:", menu_name)
            for dish in self.order[menu_name]:
                print(n, dish.get_dish_info())
                n += 1 
        print("Итого цена заказа:", self.result_price, "руб.")