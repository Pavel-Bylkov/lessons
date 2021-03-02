class Dish:
    def __init__(self, name_dish: str, weight: str, price: str) -> None:
        self.name_dish = name_dish
        self.weight = weight
        self.price = price
    
    def get_dish_info(self) -> str:
        return f"{self.name_dish} ({self.weight} гр.) - {self.price} руб."
    
    def edit_name(self) -> None:
        self.name_dish = input("Введите название блюда: ")
    
    def edit_weight(self) -> None:
        self.weight = input("Введите вес порции в граммах (только цифру): ")
    
    def edit_price(self) -> None:
        self.price = input("Введите цену за 1 порцию в рублях (только цифру): ")
    

class Menu:
    def __init__(self, menu_name: str) -> None:
        self.menu_name = menu_name
        self.list_dishes = []
    
    def add_dish(self, dish: Dish) -> None:
        if dish not in self.list_dishes:
            self.list_dishes.append(dish)
    
    def print_menu(self) -> None:
        print(f"Меню : {self.menu_name}")
        if self.list_dishes:
            print("Список блюд:")
            n = 1
            for dish in self.list_dishes:
                print(n, "-", dish.get_dish_info())
                n += 1 
        else:
            print("Список блюд пуст.")

    def edit_name(self) -> None:
        self.menu_name = input("Введите названию меню")

    def del_dish(self, number: int) -> None:
        if 1 <= number <= len(self.list_dishes):
            dish = self.list_dishes.pop(number - 1)
            print(dish.get_dish_info(), "удалено из меню")
    
    def get_dish(self, number: int) -> None:
        if 1 <= number <= len(self.list_dishes):
            return self.list_dishes.pop(number - 1)
            print(dish.get_dish_info(), "удалено из меню")

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

    def del_dish(self, del_n: int) -> None:
        n = 1
        for menu_name in self.order:
            for dish in self.order[menu_name]:
                if n == del_n:
                    self.order[menu_name].remove(dish)
                    print(dish.get_dish_info(), "удалено из заказа")
                n += 1 
