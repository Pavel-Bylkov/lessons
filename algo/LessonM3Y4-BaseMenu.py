class Menu:
    def __init__(self, menu_name):
        self.menu_name = menu_name
        self.meals_names = []
        self.meals = []

    def set_information(self, meal_name, meal):
        self.meals.append(meal)
        self.meals_names.append(meal_name)

    def get_information(self, meal_name):
        for i in range(len(self.meals_names)):
            if meal_name == self.meals_names[i]:
                return self.meals[i]
        return Meal(meal_name, 0, 0, 0)


class Meal:
    def __init__(self, meal_name, price, weight, callories):
        self.meal_name = meal_name
        self.price = price
        self.weight = weight
        self.callories = callories
        self.dish = self.meal_name + "(" + self.weight + ")" + " - " + self.price
    
    def get_dish_information(self):
        return self.dish

class Order:
    total = 0
    def __init__(self):
        self.menu_names = {}

    def append_meal(self, menu_name, meal):
        if menu_name in self.menu_names:
            self.menu_names[menu_name].append(meal)
        else:
            self.menu_names[menu_name] = [meal]
    
    def print_order(self):
        print("|","-"*100,"|", sep="")
        print("|","-"*43, "Чек", "-"*43, "|", sep="")
        for menu_name in self.menu_names:
            print("|{:100}|".format(menu_name))
            for i in range(len(self.menu_names[menu_name])):
                print("|{}. {:90}{:7}|".format(i + 1, self.menu_names[menu_name][i].meal_name, self.menu_names[menu_name][i].price))
                self.total += self.menu_names[menu_name][i].price
        print("|","-"*100,"|", sep="")
        print("|ИТОГО: {:93}|".format(self.total))
        print("|","-"*100,"|", sep="")



list_meals = {"Картофельное пюре": Meal("Картофельное пюре", 30, 200, 300),
             "Борщ": Meal("Борщ", 35, 150, 500),
             "Компот": Meal("Компот", 10, 100, 150)}
List_menu = {"Завтрак": Menu("Завтрак"), "Обед": Menu("Обед"), "Ужин": Menu("Ужин")}

List_menu["Завтрак"].set_information("Картофельное пюре", list_meals["Картофельное пюре"])
List_menu["Завтрак"].set_information("Компот", list_meals["Компот"])
List_menu["Обед"].set_information("Борщ", list_meals["Борщ"])
List_menu["Обед"].set_information("Картофельное пюре", list_meals["Картофельное пюре"])
List_menu["Ужин"].set_information("Компот", list_meals["Компот"])

print("Завтрак:", List_menu["Завтрак"].meals_names)
print("Обед:", List_menu["Обед"].meals_names)
print("Ужин:", List_menu["Ужин"].meals_names)

order = Order()
while True:
    menu_name, meal_name = tuple(input("Выберите меню, выберите блюдо через запятую:").split(","))
    if menu_name in List_menu:
        order.append_meal(menu_name, List_menu[menu_name].get_information(meal_name))
    else:
        print("Такое меню не найдено...")
    if input("Продолжить заказ (да/нет)?").lower() != "да":
        break
order.print_order() 