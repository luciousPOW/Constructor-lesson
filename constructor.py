# "Constructor" to initialize objects

class Fruits:
    def __init__(self, type, quantity, price):
        self.type = type
        self.quantity = quantity
        self.price = price
        print('Created ' + self.type)

fruitOne = Fruits('Apple',3,34.5)
print(fruitOne)
