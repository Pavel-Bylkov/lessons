class Dish:
    all_dishes = {}
    def set_dish_info(self, name_dish, weight, price):
        self.name_dish = name_dish
        self.weight = weight
        self.price = price
        Dish.all_dishes[name_dish] = self

class Menu:
    all_menu = {}
    def set_menu_info(self, menu_name):
        self.menu_name = menu_name
        self.list_dishes = []
        Menu.all_menu[menu_name] = self
    def add_dish(self, dish):
        if dish not in self.list_dishes:
            self.list_dishes.append(dish)

class Receipt:
    all_orders = {}
    def set_order(self, client_id, date):
        self.client_id = client_id
        self.date = date
        self.total_price = 0
        self.order = {}
        if client_id in Receipt.all_orders:
            Receipt.all_orders[client_id][date] = self
        else:
            Receipt.all_orders[client_id] = {date: self}
    def add_dish(self, menu_name, dish):
        if menu_name in self.order:
            self.order[menu_name].append(dish)
        else:
            self.order[menu_name] = [dish]
        self.total_price += int(dish.price)

def admin_interface():
    print("""
    Админ-панель онлайн-заказа еды.
    Вам доступны действия:
    0 - Показать список меню
    1 - Создать новое меню
    2 - Заполнить меню
    3 - Вывести меню

    """)
run = True
while run:
    pass