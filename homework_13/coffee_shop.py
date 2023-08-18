import csv

class Product:
    PRODUCT_TYPE = ['coffee', 'tea']


    @classmethod
    def validate(cls, arg):
        if arg not in cls.PRODUCT_TYPE:
            return False
        return True

    def __init__(self, name: str, price: int, prod_type: str):
        self.name = name
        self.price = price
        if self.validate(prod_type):
            self.prod_type = prod_type
        else:
            self.prod_type = 'additional'

    def __str__(self):
        return f"{self.prod_type}: {self.name}, price: {self.price};"

    def __repr__(self):
        return f"Type: {self.prod_type}; Name: {self.name}; Price: {self.price}"
        # return [self.prod_type, self.name, self.price]


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
                # print(f"{row} - has been loaded to the store")

    def _get_prod_tea(self):
        prod_list = []
        for item in self.products:
            # print(item[0].prod_type)
            if item[0].prod_type == 'tea':
                prod_list.append([item[0]])
        return prod_list

    def _get_prod_coffee(self):
        prod_list = []
        for item in self.products:
            # print(item[0].prod_type)
            if item[0].prod_type == 'coffee':
                prod_list.append([item[0]])
        return prod_list

    def _get_prod_all(self):
        prod_list = []
        for item in self.products:
            prod_list.append([item[0]])
        return prod_list

    def funcs(self, name):
        functions = {
            'tea': self._get_prod_tea(),
            'coffee': self._get_prod_coffee(),
            'all': self._get_prod_all(),
        }
        return functions[name]

    def get_products(self, name):
        for pr in self.funcs(name):
            print(" ".join(map(str, pr)), sep="\n")


# client code
# prd = Product('Чай', 10, 'tea')
# prd2 = Product('Чай', 10, 'coffee')
# print(prd)

store = Store()
store.import_inventory('inventory.csv')
# print(store.products)
# store.get_prod_tea()
print(store.products)
# store.get_products('tea')
# store.get_products('coffee')
store.get_products('all')


