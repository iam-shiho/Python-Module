#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        growth_rate: float,
        age: int
    ) -> None:
        self.name = name.capitalize()
        self.height = height
        self.growth_rate = growth_rate
        self.age = age

    def grow(self) -> None:
        self.height += self.growth_rate

    def age_count(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height,1)}cm, {self.age} days old")
        for day in range(1, 8):
            self.grow()
            self.age_count()
            print(f"=== Day {day} ===")
            print(
                f"{self.name}: {round(self.height, 1)}cm, "
                f"{self.age} days old")

        print(f"Growth this week: {round(self.growth_rate * 7,1)}cm")


def plant_grow() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 0.8, 30)
    rose.show()


if __name__ == "__main__":
    plant_grow()
