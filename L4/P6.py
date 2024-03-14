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


class Table:
    def __init__(self, tid):
        self.tid = tid
        self.turnover_count = 0
        self.occupy = 0
        self.ordered = []
        self.served = []
        self.paid = False

    def add_order(self, dish_number, menu):
        dish = menu.dishes[dish_number - 1]
        self.ordered.append(dish)

    def review_order(self):
        print("Order")
        for i, dish in enumerate(self.ordered, start=1):
            print('{}. {}. {}. {:.2f}'.format(i, dish['name'], dish['description'], dish['price']))

    def serve(self, order_number):
        dish = self.ordered.pop(order_number - 1)
        self.served.append(dish)

    def show_bill(self):
        total_price = sum(dish['price'] for dish in self.served)
        print("Bill")
        for i, dish in enumerate(self.served, start=1):
            print('{}. {}. {}. {:.2f}'.format(i, dish['name'], dish['description'], dish['price']))


        print('Total {:.2f}'.format(total_price))

    def pay_bill(self):
        self.ordered = []
        self.served = []
        self.paid = True

    def leave_table(self):
        if self.paid:
            self.occupy = 0
        else:
            print("Eat-and-Run Alert!!! Stop Them!")

    def new_customers(self, num_customers):
        if self.occupy == 0:
            self.occupy = num_customers
            self.turnover_count += 1
            self.paid = False
        else:
            print("Occupied Table Alert!!! Get Customers to Another Table!")


if __name__ == '__main__':
    m1 = Menu()
    m2 = DrinkMenu()
    t1 = Table(1)
    print(type(t1))
    print(vars(t1))
    print('\nNew Customers')
    t1.new_customers(4)
    print(vars(t1))
    m1.show()
    print('\nAdd')
    t1.add_order(2, m1)
    t1.review_order()
    print()
    m2.show()
    print('\nAdd')
    t1.add_order(3, m2)
    t1.add_order(5, m2)
    t1.review_order()
    print()
    t1.show_bill()
    print('\nServe')
    t1.serve(2)
    t1.review_order()
    t1.show_bill()
    print('\nServe')
    t1.serve(1)
    t1.review_order()
    t1.show_bill()
    print('\nLeave')
    t1.leave_table()
    t1.show_bill()
    print('\nPay')
    t1.pay_bill()
    t1.show_bill()
    print('\nNew Customers')
    t1.new_customers(2)
    print('\nLeave')
    t1.leave_table()
    print('\nNew Customers')
    t1.new_customers(3)
    print(vars(t1))
