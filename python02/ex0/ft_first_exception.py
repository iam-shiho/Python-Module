#!/usr/bin/env python3

def test_temperature() -> None:
    print('=== Garden Temperature ===')
    print()
    test = ['25', 'abc']
    for test_value in test:
        try:
            temp = input_temperature(test_value)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print()
    print("All tests completed - program didn't crash!")


def input_temperature(temp: str) -> int:
    print(f"Input data is '{temp}'")
    return int(temp)


if __name__ == "__main__":
    try:
        test_temperature()
    except Exception as e:
        print(f"Error: {e}")
