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
            print(dish.get_dish_info())
            n += 1

class Receipt:
    result = 0
    def __init__(self, name: str) -> None:
        self.name = name
        self.order = []
    def set_order(self, parametr1: str, parametr2: str) -> None:
        self.parametr1 = parametr1
        self.order.append(self.parametr1)
        self.parametr2 = parametr2
        self.result = self.result + int(self.parametr2)
    def get_order(self) -> list:
        print("Общий чек: ")
        return self.order
    def get_result(self) -> int:
        print("Итого: ")
        return self.result

br = Menu("Завтраки")
din = Menu("Ужины")
bs = Menu("Бизнес-ланчи")
check = Receipt("Сделать заказ")