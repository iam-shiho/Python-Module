#!/usr/bin/env python3

import sys
import typing

class None_value(Exception):
    pass


def read_file(file_name: str) -> typing.IO:
    return open(file_name, 'r')


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) < 2:
        raise None_value("Usage: ft_ancient_text.py <file>")
    file_name = sys.argv[1]
    try:
        print(f"Accessing file '{file_name}'")
        r_file = read_file(file_name)
        contents = r_file.read()
        print("---")
        print()
        print(contents)
        print("---")
        r_file.close()
        print(f"File '{file_name}' closed.")
        print("Transform data:")
        print("---")
        print(contents)
        print("---")
        new_file = input("Enter new file name (or empty):")
        if not new_file:
            raise None_value("Not saving data.")
        print(f"Saving data to '{new_file}'")
        print(f"Data saved in file '{new_file}'.")
    except FileNotFoundError as e:
        print(f"Error opening file '{file_name}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{file_name}': {e}")
    except IsADirectoryError as e:
        print(f"Error opening file '{file_name}': {e}")
    except None_value as e:
        print(e)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
