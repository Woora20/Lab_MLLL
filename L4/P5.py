class Menu:
    def __init__(self):
        self.name = "Tasty and Healthy"
        self.dishes = [
            {'name': 'Kang Saparot', 'description': 'Mussel pineapple curry', 'price': 120},
            {'name': 'Jeolhon', 'description': 'Basil spicy hotpot', 'price': 200},
            {'name': 'Sup Kanoon', 'description': 'Smashed jackfruit salad', 'price': 50}
        ]

    def show(self):
        print(self.name)
        for index, dish in enumerate(self.dishes, start=1):
            print('{:d}. {:s}. {:s}. {:.2f}'.format(
                index, dish['name'], dish['description'], dish['price']))

    def new_dish(self, dish_dict):
        self.dishes.append(dish_dict)

    def remove_dish(self, dish_number):
        if 1 <= dish_number <= len(self.dishes):
            del self.dishes[dish_number - 1]

    def update_price(self, dish_number, new_price):
        if 1 <= dish_number <= len(self.dishes):
            self.dishes[dish_number - 1]['price'] = new_price


class DrinkMenu(Menu):
    def __init__(self):
        super().__init__()
        self.name = "Drinks"
        self.dishes = [
            {'name': 'Oolong tea', 'description': 'Legendary Oolong', 'price': 40, 'serve_hot': True},
            {'name': 'English tea', 'description': 'English afternoon tea', 'price': 30, 'serve_hot': True},
            {'name': 'Strawberry yogurt', 'description': 'Refreshing strawberry drinking yogurt', 'price': 50, 'serve_hot': False},
            {'name': 'Matoom juice', 'description': 'Toxic-cleansing bael juice', 'price': 20, 'serve_hot': False},
            {'name': 'Ginger tea', 'description': 'Ginger tea, good for digestion', 'price': 45, 'serve_hot': True}
        ]

    def show_hot(self):
        print(self.name)
        for index, dish in enumerate(self.dishes, start=1):
            if dish['serve_hot']:
                print('{:d}. {:s}. {:s}. {:.2f}'.format(
                    index, dish['name'], dish['description'], dish['price']))

    def show_cold(self):
        print(self.name)
        for index, dish in enumerate(self.dishes, start=1):
            if not dish['serve_hot']:
                print('{:d}. {:s}. {:s}. {:.2f}'.format(
                    index, dish['name'], dish['description'], dish['price']))


if __name__ == '__main__':
    m1 = DrinkMenu()
    print(type(m1))
    print(type(m1).__bases__, '\n')
    m1.show()
    print('\nNew')
    m1.new_dish({'name': 'Kajiab juice', 'description': 'Anti-oxidant roselle juice', 'price': 25, 'serve_hot': False})
    m1.show()
    print('\nHot')
    m1.show_hot()
    print('\nCold')
    m1.show_cold()
