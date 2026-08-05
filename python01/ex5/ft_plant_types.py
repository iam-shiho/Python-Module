#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def age(self, days: int) -> None:
        self.plant_age += days

    def grow(self, grow_height: float) -> None:
        self.height += grow_height


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def show(self) -> None:
        super().show()
        print(f' Color: {self.color}')
        if self.blooming:
            print(f' {self.name} is blooming beautifully!')
        else:
            print(f' {self.name} has not bloomed yet')

    def bloom(self) -> None:
        self.blooming = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f' Trunk diameter: {round(self.trunk_diameter,1)}cm')

    def produce_shade(self) -> None:
        print(f'Tree {self.name} now produces a shade of '
              f'{round(self.height,1)}cm long and '
              f'{round(self.trunk_diameter,1)}cm wide.')


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f' Harvest season: {self.harvest_season}')
        print(f' Nutritional value: {self.nutritional_value}')

    def add_age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value = days

    def add_grow(self, grow_height: float) -> None:
        super().grow(grow_height)


def print_data():
    print('===  Garden Plant Types ===')
    print('=== Flower')
    rose = Flower('Rose', 15.0, 10, 'red')
    rose.show()
    print('[asking the rose to bloom]')
    rose.bloom()
    rose.show()

    print()
    print('=== Tree')
    oak = Tree('Oak', 200.0, 365, 5.0)
    oak.show()
    print('[asking the oak to produce shade]')
    oak.produce_shade()

    print()
    print('=== Vegetable')
    tomato = Vegetable('Tomato', 5.0, 10, 'April')
    tomato.show()
    print('[make tomato grow and age for 20 days]')
    tomato.add_age(20)
    tomato.add_grow(42.0)
    tomato.show()


if __name__ == "__main__":
    print_data()
