#!/usr/bin/env python3

class Plant:

    class Statistics:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def stats_print(self) -> None:
            print(f'Stats: {self.grow_count} grow, '
                  f'{self.age_count} age, {self.show_count} show')

    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.plant_age = plant_age
        self.statistics = self.Statistics()

    @staticmethod
    def check_year_old(age: int) -> None:
        if age >= 365:
            print(f'Is {age} days more than a year? -> True')
        else:
            print(f'Is {age} days more than a year? -> False')

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")
        self.statistics.show_count += 1

    def age(self, days: int) -> None:
        self.plant_age += days
        self.statistics.age_count += 1

    def grow(self, grow_height: float) -> None:
        self.height += grow_height
        self.statistics.grow_count += 1

    @classmethod
    def anonymous_class(
        cls,
        name: str = 'Unknown plant',
        height: float = 0.0,
        plant_age: int = 0
    ) -> 'Plant':
        return cls(name, height, plant_age)

    def stats(self) -> None:
        self.statistics.stats_print()


class Flower(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        color: str
    ) -> None:
        super().__init__(name, height, plant_age)
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
        plant_age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter
        self.produce_shade_count = 0

    def show(self) -> None:
        super().show()
        print(f' Trunk diameter: {round(self.trunk_diameter,1)}cm')

    def produce_shade(self) -> None:
        print(f'Tree {self.name} now produces a shade of '
              f'{round(self.height,1)}cm long and '
              f'{round(self.trunk_diameter,1)}cm wide.')
        self.produce_shade_count += 1

    def stats_produce_shade(self) -> None:
        super().stats()
        print(f' {self.produce_shade_count} shade')


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        color: str
    ) -> None:
        super().__init__(name, height, plant_age, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f' Seeds: {self.seeds}')

    def bloom_and_seed(self, seeds) -> None:
        if not self.blooming:
            self.seeds = seeds
        self.blooming = True


def print_data():
    print('=== Garden statistics ===')
    print('=== Check year-old')
    Plant.check_year_old(30)
    Plant.check_year_old(400)
    print()
    print('=== Flower')
    rose = Flower('Rose', 15.0, 10, 'red')
    rose.show()
    print('[statistics for Rose]')
    rose.stats()
    print('[asking the rose to grow and bloom]')
    rose.bloom()
    rose.grow(8.0)
    rose.show()
    print('[statistics for Rose]')
    rose.stats()

    print()
    print('=== Tree')
    oak = Tree('Oak', 200.0, 365, 5.0)
    oak.show()
    print('[statistics for Oak]')
    oak.stats_produce_shade()
    print('[asking the oak to produce shade]')
    oak.produce_shade()
    print('[statistics for Oak]')
    oak.stats_produce_shade()

    print()
    print('=== Seed')
    sunflower = Seed('Sunflower', 80.0, 45, 'yellow')
    sunflower.show()
    print('[make sunflower grow, age and bloom]')
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom_and_seed(42)
    sunflower.show()
    print('[statistics for Sunflower]')
    sunflower.stats()

    print()
    print('=== Anonymous')
    anonymous = Plant.anonymous_class()
    anonymous.show()
    print('[statistics for Unknown plant]')
    anonymous.stats()


if __name__ == "__main__":
    print_data()
