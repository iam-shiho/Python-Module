#!/usr/bin/env python3

def test_temperature() -> None:
    test = ['25', 'abc', '100', '-50']
    for test_value in test:
        input_temperature(test_value)
        print()
    print("All tests completed - program didn't crash!")


def input_temperature(temp: str) -> None:

    print(f"Input data is '{temp}'")
    try:
        int(temp)
    except ValueError:
        return print(f"Caught input_temperature error: "
              f"invalid literal for int() with base 10: '{temp}'")
    if int(temp) > 40:
        return print(f'Caught input_temperature error: {int(temp)}°C is too hot for plants (max 40°C)')
    elif int(temp) < 0:
        return print(f'Caught input_temperature error: {int(temp)}°C is too cold for plants (min 0°C)')
    else:
        print(f'Temperature is now {int(temp)}°C')


if __name__ == "__main__":
    print('===  Garden Temperature Checker ===')
    print()
    test_temperature()
