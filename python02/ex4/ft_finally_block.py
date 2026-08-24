#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = 'Unknown plant error') -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if not plant_name.capitalize() == plant_name:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f'Watering {plant_name}: [OK]')


def test_watering_system(plants: list[str]) -> None:
    print('Opening watering system')
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f'Caught PlantError: {e}')
        print(".. ending tests and returning to main")
    finally:
        print('Closing watering system')


def main() -> None:
    print('=== Garden Watering System ===')
    print()
    print('Testing invalid plants...')
    plants = ['Tomato', 'Lettuce', 'Carrots']
    test_watering_system(plants)
    print()
    print('Testing invalid plants...')
    plants = ['Tomato', 'lettuce', 'Carrots']
    test_watering_system(plants)
    print()
    print('Cleanup always happens, even with errors!')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
