class Menu:
    def __init__(self):
        self.name = ""
        self.dishes = [{'name': '', 'description': '', 'price': 0}]

if __name__ == '__main__':
    print(type(Menu))
    
    m1 = Menu()
    print(type(m1))
    
    m1.name = "Tasty and Healthy"
    m1.dishes = [
        {'name': 'Kang Saparot', 'description': 'Mussel pineapple curry', 'price': 120},
        {'name': 'Jeolhon', 'description': 'Basil spicy hotpot', 'price': 200}
    ]
    
    print(m1.name)
    for d in m1.dishes:
        print('*', d)
