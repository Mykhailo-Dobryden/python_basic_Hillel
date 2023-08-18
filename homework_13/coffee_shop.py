import csv
from tabulate import tabulate


class Product:
    PRODUCT_TYPE = ['coffee', 'tea']
    LATTE = ['Молоко', 'Еспресо']

    # @classmethod
    # def validate(cls, arg):
    #     if arg not in cls.PRODUCT_TYPE:
    #         return False
    #     return True

    @staticmethod
    def _validate(prod_type):
        if prod_type not in Product.PRODUCT_TYPE:
            return False
        return True

    def __init__(self, name: str, price: int, prod_type: str):
        self.name = name
        self.price = price
        if self._validate(prod_type):
            self.prod_type = prod_type
        else:
            self.prod_type = 'additional'

    def __str__(self):
        return f"{self.prod_type}: {self.name}, price: {self.price};"

    def __repr__(self):
        return f"Type: {self.prod_type}; Name: {self.name}; Price: {self.price}"

    def __add__(self, other):
        name = None
        price = None
        prod_type = None
        if self.name and other.name in Product.LATTE:
            name = 'Латте'
            price = self.price + other.price
            prod_type = "coffee"
            return Product(name, price, prod_type)
        raise ArithmeticError(f"You can't create a Latte from {self.name} and {other.name}")


class Store:
    def __init__(self, name="Coffe&Tea"):
        self.name = name
        self.products = []

    def __str__(self):
        return f"{self.name} shop"

    def import_inventory(self, path_to_file: str):
        with open(f"{path_to_file}", 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                name = row[0]
                pr_type = row[1]
                price = int(row[2])
                amount = 5
                if row[3]:
                    amount = int(row[3])
                p = Product(name, price, pr_type)
                self.products.append((p, amount))

    def get_products(self, name: str = 'all') -> str:
        prod_list = []
        headers = ["Назва", "Тип", "Ціна", "Кількість"]
        for item in self.products:
            if name == 'all':
                prod_list.append([item[0].name, item[0].prod_type, item[0].price, item[1]])
            elif item[0].prod_type == name:
                prod_list.append([item[0].name, item[0].prod_type, item[0].price, item[1]])
        return tabulate(prod_list, headers=headers)

    def get_total_cost(self) -> str:
        cost = 0
        for item, amount in self.products:
            cost += item.price * amount
        return f"Total price of all goods is: {cost} UAH"

    def sell_product(self, name):
        for item in self.products:
            if item[0].name == name:
                self.products.pop(self.products.index(item))
                return print(f"{name} has been sold")


# _______________________client code_____________________:
if __name__ == '__main__':

    store = Store()
    store.import_inventory('inventory.csv')
    # print(store.products)
    print(store.get_total_cost())
    # print(store.get_products('all'))
    # store.sell_product('Хліб')
    store.sell_product('Зелений чай')
    # store.sell_product('Молоко')
    print(store.get_products())
    print(store.get_total_cost())

    milk = Product('Молоко', 10, 'additional')
    espresso = Product('Еспресо', 25, prod_type='coffee')
    latte = espresso + milk
    print(latte)

    # latte2 = milk + espresso
    # print(latte2)
    # corn = Product('Кукурудза', 2, 'additional')
    # latte3 = milk + corn
    # print(latte3)


