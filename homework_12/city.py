from dataclasses import dataclass
import random
from tabulate import tabulate
import names



@dataclass
class Building:
    build_number: int
    residents: int


@dataclass
class Street:
    street_name: str
    buildings = [Building(num, random.randint(1, 100)) for num in range(1, random.randint(5, 20))]
    # buildings = [1, 2, 3, 4, 5]


@dataclass
class City:
    name: str = "Odesa"
    # streets: int = 10
    # street_arr = [Street(f"{names.get_last_name()} street") for n in range(1, streets)]
    street_arr = []

    # def add_street(self):
    #     pass

    def create_random_streets(self, number: int):
        # streets = [Street(f"{names.get_last_name()} street") for n in range(1, number + 1)]
        for num in range(1, number + 1):
            self.street_arr.append(Street(f"{names.get_last_name()} street"))
        return self.street_arr

    def get_residents(self):
        residents = 0
        for street in self.street_arr:
            for building in street.buildings:
                residents += building.residents
        return residents

    def get_city_table(self):
        header = ["Street", "Building Num", "Residents"]
        table = []
        for street in self.street_arr:
            for building in street.buildings:
                table.append([street.street_name, building.build_number, building.residents])

        return tabulate(table, headers=header)


c = City('Rozdilna')
print(c)
c.create_random_streets(10)
print(c.street_arr)
print(c.get_residents())
print(c.get_city_table())

# strit = Street('volvo')
# print(strit)
# print(strit.buildings)
