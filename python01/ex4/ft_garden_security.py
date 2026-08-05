#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float = 15.0, age: int = 10) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age
        print(f"Plant created: {self.name}: {round(self.height,1)}cm, "
              f"{self.age} days old")

    def show(self) -> None:
        print(f"Current state: {self.name}: {round(self.height,1)}cm, "
              f"{self.age} days old")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return
        else:
            self.height = height
            print(f'Height updated: {round(self.height)}cm')
            return

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return
        else:
            self.age = age
            print(f'Age updated: {self.age} days')
            return

    def get_height(self, height: float) -> None:
        print('Height update rejected')

    def get_age(self, age: int) -> None:
        print('Age update rejected')


def print_data():
    print('=== Garden Security System ===')
    rose = Plant("Rose", 15.0, 10)
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-25.0)
    rose.get_height(25.0)
    rose.set_age(-30)
    rose.get_age(30)
    print()
    rose.show()


if __name__ == "__main__":
    print_data()
