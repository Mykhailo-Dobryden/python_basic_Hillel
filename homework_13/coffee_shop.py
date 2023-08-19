"""Написати програму кавовий магазин.
Об'єкти:
  Product
  - тип може бути тільки coffee, tea, або additional (не можна створити об'єкт з іншим типом)
  - властивості: найменування, тип, ціна
  - print об'єкта продукту повинен повертати "Кава: Еспресо, ціна: 27грн."
  Store
  - може імпортувати продукти із файлу invertory.csv
  (за замовчуванням по 5 шт. кожного найменування, або вказану кількість)
  - може повернути список продуктів потрібного типу (tea, coffee чи всі продукти)
  - може повернути загальну вартість продуктів
  - може продати продукт
* Зробити можливість поєднання типів Espresso та Молоко, у підсумку повинно повернути об'єкт Latte """


import csv
from tabulate import tabulate


class Product:
    """
    Represents a product available in the coffee shop.

    Attributes:
        name (str): The name of the product.
        price (int): The price of the product.
        prod_type (str): The type of the product (coffee, tea, or additional).
    """
    PRODUCT_TYPE = ['coffee', 'tea']
    LATTE = ['Молоко', 'Еспресо']

    @staticmethod
    def _validate(prod_type):
        """
        Validates the product type.

        Args:
            prod_type (str): The type of the product (coffee, tea, or additional).

        Returns:
            bool: True if the product type is valid, False otherwise.
        """
        if prod_type not in Product.PRODUCT_TYPE:
            return False
        return True

    def __init__(self, name: str, price: int, prod_type: str):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            price (int): The price of the product.
            prod_type (str): The type of the product.
        """
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
        """
        Creates a new Latte product by combining Espresso and Milk.

        Args:
            other (Product): Another product instance.

        Returns:
            Product: A new Latte product instance.

        Raises:
            ArithmeticError: If Latte cannot be created from the given products.
        """
        if self.name and other.name in Product.LATTE:
            name = 'Латте'
            price = self.price + other.price
            prod_type = "coffee"
            return Product(name, price, prod_type)
        raise ArithmeticError(f"You can't create a Latte from {self.name} and {other.name}")


class Store:
    """
    Represents a coffee shop store.

    Attributes:
        name (str): The name of the store.
        products (list): List of product instances available in the store.
    """
    def __init__(self, name="Coffe&Tea"):
        self.name = name
        self.products = []

    def __str__(self):
        return f"{self.name} shop"

    def import_inventory(self, path_to_file: str):
        """
        Imports products and their inventory from a CSV file.

        Args:
            path_to_file (str): The path to the CSV file.
        """
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
        """
        Gets a list of products filtered by product type (coffe, tea, additional, all).

        Args:
            name (str): The type of products to retrieve ('all' for all products).

        Returns:
            str: A formatted table with the list of products.
                """
        prod_list = []
        headers = ["Назва", "Тип", "Ціна", "Кількість"]
        for item in self.products:
            if name == 'all':
                prod_list.append([item[0].name, item[0].prod_type, item[0].price, item[1]])
            elif item[0].prod_type == name:
                prod_list.append([item[0].name, item[0].prod_type, item[0].price, item[1]])
        return tabulate(prod_list, headers=headers)

    def get_total_cost(self) -> str:
        """
        Calculates the total cost of all products in the store.

        Returns:
            str: A string indicating the total cost.
        """
        cost = 0
        for item, amount in self.products:
            cost += item.price * amount
        return f"Total price of all goods is: {cost} UAH"

    def sell_product(self, name):
        """
        Sells a product from the store.

        Args:
            name (str): The name of the product to be sold (actually product will be
            removed from attribute products).
        """
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

    print(store.get_total_cost())

    milk = Product('Молоко', 10, 'additional')
    espresso = Product('Еспресо', 25, prod_type='coffee')
    latte = espresso + milk
    latte2 = milk + espresso
    print(latte)
    print(latte2)
    print(store.get_products('additional'))

    # latte2 = milk + espresso
    # print(latte2)
    # corn = Product('Кукурудза', 2, 'additional')
    # latte3 = milk + corn
    # print(latte3)
