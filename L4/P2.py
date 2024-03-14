class Menu:
    def __init__(self):
        self.name = ""
        self.dishes = [{'name': '', 'description': '', 'price': 0}]

    def show(self):
        print(self.name)
        for index, dish in enumerate(self.dishes, start=1):
            print('{:d}. {:s}. {:s}. {:.2f}'.format(
                index, dish['name'], dish['description'], dish['price']))

if __name__ == '__main__':
    m1 = Menu()
    m1.name = "Tasty and Healthy"
    m1.dishes = [
        {'name': 'Kang Saparot', 'description': 'Mussel pineapple curry', 'price': 120},
        {'name': 'Jeolhon', 'description': 'Basil spicy hotpot', 'price': 200}
    ]
    m1.show()
