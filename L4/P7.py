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
        if 1 <= dish_number <= len(menu.dishes):
            self.ordered.append((dish_number, menu))

    def review_order(self):
        print("Order")
        for order in self.ordered:
            dish_number, menu = order
            dish = menu.dishes[dish_number - 1]
            print('{:d}. {:s}. {:s}. {:.2f}'.format(
                dish_number, dish['name'], dish['description'], dish['price']))

    def serve(self, order_number):
        if 1 <= order_number <= len(self.ordered):
            self.served.append(self.ordered.pop(order_number - 1))

    def show_bill(self):
        total_price = 0
        print("Bill")
        for order in self.served:
            dish_number, menu = order
            dish = menu.dishes[dish_number - 1]
            print('{:d}. {:s}. {:.2f}'.format(dish_number, dish['name'], dish['price']))
            total_price += dish['price']
        print('Total {:.2f}'.format(total_price))
        return total_price

    def pay_bill(self):
        self.ordered = []
        self.served = []
        self.paid = True

    def leave_table(self):
        if self.paid:
            self.occupy = 0
        else:
            print("Eat-and-Run Alert!!! Stop Them!")

    def new_customers(self, num_people):
        if self.occupy == 0:
            self.occupy = num_people
            self.turnover_count += 1
            self.paid = False
        else:
            print("Occupied Table Alert!!! Get Customers to Another Table!")

class Cashier:
    def __init__(self):
        self.Tables = []
        self.revenue = 0

    def new_table(self):
        self.Tables.append(Table(len(self.Tables) + 1, self))

    def close_table(self, table_number):
        table = self.Tables.pop(table_number - 1)
        table.occupy = 0
        table.ordered = []
        table.served = []
        table.paid = False

    def show_status(self):
        print('All table statuses')
        print('{:>6}. {:>10}. {:>10}.'.format('Table', 'Turn-over', 'Occupancy'))
        for i, table in enumerate(self.Tables, start=1):
            print('{:>6}. {:>10}. {:>10}.'.format(i, table.turnover_count, table.occupy))

    def show_revenue(self):
        print('Current revenue = {:.2f}'.format(self.revenue))

    def update_revenue(self, amount):
        self.revenue += amount


class Table:
    def __init__(self, tid, cashier):
        self.tid = tid
        self.turnover_count = 0
        self.occupy = 0
        self.ordered = []
        self.served = []
        self.paid = False
        self.cashier = cashier

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
        self.cashier.update_revenue(total_price)

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
    cashier = Cashier()
    print(type(cashier))
    print(vars(cashier))
    print('\nNew table')
    cashier.new_table()
    print('\nNew table')
    cashier.new_table()
    cashier.show_status()
    m1 = Menu()
    m2 = DrinkMenu()
    cashier.Tables[0].new_customers(3)
    cashier.show_status()
    cashier.Tables[1].new_customers(1)
    cashier.show_status()
    cashier.Tables[0].add_order(1, m1)
    cashier.Tables[0].add_order(2, m1)
    cashier.Tables[0].add_order(2, m1)
    cashier.Tables[0].add_order(1, m2)
    cashier.Tables[0].add_order(2, m2)
    cashier.Tables[0].add_order(3, m2)
    cashier.Tables[0].review_order()
    cashier.Tables[1].add_order(3, m1)
    cashier.Tables[1].add_order(4, m2)
    cashier.Tables[1].review_order()
    for i in range(6):
        cashier.Tables[0].serve(1)
    for i in range(2):
        cashier.Tables[1].serve(1)
    cashier.Tables[0].pay_bill()
    cashier.show_revenue()

    cashier.Tables[1].pay_bill()
    cashier.show_revenue()
    print('\nLeave')
    cashier.Tables[0].leave_table()
    cashier.show_status()
    print('\nLeave')
    cashier.Tables[1].leave_table()
    cashier.show_status()
    print('\nNew customers')
    cashier.Tables[1].new_customers(5)
    cashier.show_status()
    print('\nNew customers')
    cashier.Tables[0].new_customers(2)
    cashier.show_status()
    print('\nNew table')
    cashier.new_table()
    cashier.show_status()
    print('\nNew table')
    cashier.new_table()
    cashier.show_status()
    print('\nNew customers')
    cashier.Tables[3].new_customers(7)
    cashier.show_status()
    print('\nNew customers')
    cashier.Tables[2].new_customers(12)
    cashier.show_status()
    print('\nClose table')
    cashier.close_table(2)
    cashier.show_status()
