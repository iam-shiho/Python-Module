#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
                f"Created: {self.name}: {round(self.height, 1)}cm, "
                f"{self.age} days old"
        )


def print_plants() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()


if __name__ == "__main__":
    print_plants()
