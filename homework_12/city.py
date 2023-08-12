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
        self.buildings = [Building(number) for number in range(1, random.randint(5, 21))]

    def __repr__(self):
        return f"Street's name: {self.name}, Quantity of house: {self.buildings.__len__()} || "


class City:
    def __init__(self, name='Odesa'):
        self.name = name
        self.streets_arr = []

    def __repr__(self):
        return f"{self.name} which has {self.streets_arr.__len__()} streets: {self.streets_arr}"

    def add_street(self, name: str):
        self.streets_arr.append(Street(name))

    def del_street(self, name: str):
        for street in self.streets_arr:
            if street.name == name:
                index = self.streets_arr.index(street)
                self.streets_arr.pop(index)
                print(f"{name} street was deleted")

    def add_building(self, street_name, building_number):
        for street in self.streets_arr:
            if street.name == street_name:
                for building in street.buildings:
                    if building.number == building_number:
                        return print(f"Building with number '{building_number}' exists")

            if street.name == street_name:
                street.buildings.append(Building(building_number))
                print(f"House {building_number} has been added on {street_name} street")

    def del_building(self, street_name, building_number):
        for street in self.streets_arr:
            if street.name == street_name:
                for building in street.buildings:
                    if building.number == building_number:
                        index = street.buildings.index(building)
                        street.buildings.pop(index)
                        return print(f"House {building_number} has been removed")
                return print(f"There isn't house with {building_number}")



    def create_random_streets(self, number: int):
        if number <= 0:
            raise ValueError("An amount of streets must be positive integer")
        for num in range(1, number + 1):
            self.streets_arr.append(Street(f"{names.get_last_name()}"))
        return self.streets_arr

    def get_residents(self):
        total_residents = sum(buildings.residents for street in self.streets_arr for buildings in street.buildings)
        return total_residents

    def print_city_table(self):
        header = ["Street", "Building Num", "Residents"]
        table = []
        for street in self.streets_arr:
            for building in street.buildings:
                table.append([street.name, building.number, building.residents])
        return tabulate(table, headers=header, tablefmt="outline")


# Client's code:

if __name__ == "__main__":
    try:
        c = City('Rozdilna')
        print(c)
        c.add_street("Korolyova")
        c.add_street("Viliamsa")
        c.add_street("Oficerska")
        c.add_street("Glushko")
        c.add_building("Glushko", 1)
        c.add_building("Glushko", 20)
        c.add_building("Glushko", 302)
        c.add_building("Glushko", 101)
        c.add_building("Glushko", 103)
        c.del_building("Glushko", 1)
        c.del_building("Glushko", 101)
        c.del_building("Glushko", 77)
        c.add_building('Krakozabla', 777)
        print(c.streets_arr)
        # print(c.print_city_table())


    except ValueError as e:
        print(e)

