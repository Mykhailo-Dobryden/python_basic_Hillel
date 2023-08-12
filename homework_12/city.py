"""Написати програму Місто.
   У міста є вулиці та будинки та можливості їх додавати та видаляти.
   Вулиці можуть умістити випадкову кількість будинків від 5 до 20.
   Будинки можуть мати випадкову кількість населення від 1 до 100 осіб.
   Має бути можливість заповнити місто одним методом.
   У міста має бути атрибут, який поверне кількість населення.
   А також метод для друкування таблиці:
   Вулиця Будинок Населення
   1 1 5
   1 2 10
   1 3 25
   2 1 22
   ...
** Форматувати таблицю можна довільно, а також можна використати сторонній модуль tabulate"""

import random
from tabulate import tabulate
import names


class Building:
    """Represents a building with a specific number and random number of residents.

        Args:
            number (int): The number of the building.

        Attributes:
            number (int): The number of the building.
            residents (int): Random number of residents in the building.

        Returns:
            str: A formatted string representing the building.
        """
    def __init__(self, number: int):
        self.number = number
        self.residents = random.randint(1, 101)

    def __repr__(self):
        return f"Number of house: {self.number} | Residents: {self.residents}"


class Street:
    """Represents a street with a specific name and random number of buildings.

        Args:
            name (str): The name of the street.

        Attributes:
            name (str): The name of the street.
            buildings (list): List of Building objects on the street.

        Returns:
            str: A formatted string representing the street.
        """
    def __init__(self, name: str):
        self.name = name
        self.buildings = [Building(number) for number in range(1, random.randint(5, 21))]

    def __repr__(self):
        return f"Street's name: {self.name}, Quantity of house: {self.buildings.__len__()} || "


class City:
    """Represents a city with streets and buildings, providing various operations.

        Args:
            name (str, optional): The name of the city. Defaults to 'Odesa'.

        Attributes:
            name (str): The name of the city.
            streets_arr (list): List of Street objects in the city.

        Returns:
            str: A formatted string representing the city.
        """
    def __init__(self, name='Odesa'):
        self.name = name
        self.streets_arr = []

    def __repr__(self):
        return f"{self.name} which has {self.streets_arr.__len__()} streets: {self.streets_arr}"

    def is_street_exist(self, street_name: str) -> bool:
        """Check if a street with the given name exists in the city.

        Args:
            street_name (str): The name of the street to check.

        Returns:
            bool: True if the street exists, False otherwise.
        """
        for street in self.streets_arr:
            if street.name == street_name:
                return True
        return False

    def is_building_exist(self, street_name: str, number: int) -> bool:
        """Check if a building with the given number exists on a specific street.

        Args:
            street_name (str): The name of the street to check.
            number (int): The number of the building to check.

        Returns:
            bool: True if the building exists, False otherwise.
        """
        for street in self.streets_arr:
            if street.name == street_name:
                for building in street.buildings:
                    if building.number == number:
                        return True
                return False

    def add_street(self, street_name: str):
        """Add a new Street object to the city.street_arr.

        Args:
            street_name (str): The name of the street to add.
        """
        if self.is_street_exist(street_name) is False:
            print(f"{street_name} street has been added")
            return self.streets_arr.append(Street(street_name))
        return print(f"{street_name} street exist already")

    def del_street(self, street_name: str):
        """Delete a Street object from the city.street_arr.

        Args:
            street_name (str): The name of the street to delete.
        """
        if self.is_street_exist(street_name) is False:
            print(f"You can't delete {street_name} street, because it doesn't exist yet")
        for street in self.streets_arr:
            if street.name == street_name:
                index = self.streets_arr.index(street)
                self.streets_arr.pop(index)
                print(f"{street_name} street was deleted")

    def add_building(self, street_name: str, building_number: int):
        """Add a building to a specific street in the city.

        Args:
            street_name (str): The name of the street to add the building.
            building_number (int): The number of the building to add.
        """
        if not self.is_building_exist(street_name, building_number):
            for street in self.streets_arr:
                if street.name == street_name:
                    street.buildings.append(Building(building_number))
                    return print(f"Building {building_number} has been added on {street_name} street")
        return print(f"Building with number '{building_number}' is existing already")

    def del_building(self, street_name: str, building_number: int):
        """Delete a specific building from a specific street in the city.

        Args:
            street_name (str): The name of the street containing the building.
            building_number (int): The number of the building to delete.
        """
        if not self.is_building_exist(street_name, building_number):
            return print(f"It's impossible to delete not existing building on {street_name}, {building_number}")
        else:
            for street in self.streets_arr:
                if street.name == street_name:
                    for building in street.buildings:
                        if building.number == building_number:
                            index = street.buildings.index(building)
                            street.buildings.pop(index)
                            return print(f"Building {building_number} has been removed")

    def create_random_streets(self, number: int) -> list:
        """Create a specified number of random streets and add them to the city.

       Args:
           number (int): The number of random streets to create.

       Returns:
           list: List of created Street objects.

       Raises:
           ValueError: If the provided number is not a positive integer.
       """
        if number <= 0:
            raise ValueError("An amount of streets must be positive integer")
        for num in range(1, number + 1):
            self.streets_arr.append(Street(f"{names.get_last_name()}"))
        return self.streets_arr

    def get_residents(self) -> int:
        """Get the total number of residents in the city.

        Returns:
            int: Total number of residents in the city.
        """
        total_residents = sum(buildings.residents for street in self.streets_arr for buildings in street.buildings)
        return total_residents

    def print_city_table(self) -> str:
        """Generate and format a table with information about streets and buildings in the city.

        Returns:
            str: Formatted table representing the city's streets and buildings.
        """
        header = ["Street", "Building Num", "Residents"]
        table = []
        for street in self.streets_arr:
            for building in street.buildings:
                table.append([street.name, building.number, building.residents])
        return tabulate(table, headers=header, tablefmt="outline")


# Client's code:

if __name__ == "__main__":

    c = City('Rozdilna')
    print(c)
    c.add_street("Korolyova")
    c.add_street("Viliamsa")
    c.add_street("Oficerska")
    c.add_street("Glushko")
    c.add_street("Glushko")
    print(c.streets_arr)
    c.add_building("Glushko", 100)
    c.add_building("Glushko", 100)
    c.del_building("Glushko", 100)
    c.del_building("Glushko", 100)
    # print(c.print_city_table())
    # c.create_random_streets(3)
    # print(c.print_city_table())
    # print(c.get_residents())

