import random
from tabulate import tabulate
import names


class Building:
    def __init__(self, number):
        self.number = number
        self.residents = random.randint(1, 101)

    def __repr__(self):
        return f"Number of house: {self.number} | Residents: {self.residents}"


class Street:
    def __init__(self, name):
        self.name = name
        self.buildings = [Building(i) for i in range(1, random.randint(5, 21))]

    def __repr__(self):
        return f"Street's name: {self.name}, Quantity of house: {self.buildings.__len__()} || "


class City:
    def __init__(self, name='Odesa'):
        self.name = name
        self.street_arr = []

    def add_street(self, name: str):
        self.street_arr.append(Street(name))

    def del_street(self, name: str):
        for street in self.street_arr:
            if street.name == name:
                index = self.street_arr.index(street)
                self.street_arr.pop(index)
                print(f"{name} street was deleted")

    def create_random_streets(self, number: int):
        if number <= 0:
            raise ValueError("An amount of streets must be positive integer")
        for num in range(1, number + 1):
            self.street_arr.append(Street(f"{names.get_last_name()}"))
        return self.street_arr

    def get_residents(self):
        total_residents = sum(buildings.residents for street in self.street_arr for buildings in street.buildings)
        return total_residents

    def get_city_table(self):
        header = ["Street", "Building Num", "Residents"]
        table = []
        for street in self.street_arr:
            for building in street.buildings:
                table.append([street.name, building.number, building.residents])

        return tabulate(table, headers=header)


# Client's code:

if __name__ == "__main__":
    try:
        c = City('Rozdilna')
        print(c)
        c.add_street("Korolyova")
        c.add_street("Viliamsa")
        c.add_street("Oficerska")
        c.add_street("Glushko")
        print(c.street_arr)
        # print(c.get_residents())
        c.create_random_streets(2)
        print(c.get_city_table())
        c.del_street('Glushko')
        print(c.get_residents())

        c2 = City()
        print(c2.name)
        print(c2.street_arr)
        c2.create_random_streets(7)
        c2.add_street("trolololo")
        print(c2.get_city_table())

    except ValueError as e:
        print(e)

