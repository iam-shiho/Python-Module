#!/usr/bin/env python3

def test_temperature() -> None:
    test = ['25', 'abc']
    for test_value in test:
        input_temperature(test_value)
        print()
    print("All tests completed - program didn't crash!")


def input_temperature(temp: str) -> None:

    print(f"Input data is '{temp}'")
    try:
        int(temp)
        print(f'Temperature is now {int(temp)}°C')
    except ValueError:
        print(f"Caught input_temperature error: "
              f"invalid literal for int() with base 10: '{temp}'")


if __name__ == "__main__":
    print('=== Garden Temperature ===')
    print()
    test_temperature()
