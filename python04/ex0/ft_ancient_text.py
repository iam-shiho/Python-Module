#!/usr/bin/env python3

import sys


class None_value(Exception):
    pass


def cat_file() -> None:
    if len(sys.argv) < 2:
        raise None_value("Usage: ft_ancient_text.py <file>")
    file_name = sys.argv[1]
    try:
        print(f"Accessing file '{file_name}'")
        r_file = open(file_name, 'r')
        contents = r_file.read()
        print("---")
        print()
        print(contents)
        print()
        print("---")
        r_file.close()
        print(f"File '{file_name}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{file_name}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{file_name}': {e}")
    except IsADirectoryError as e:
        print(f"Error opening file '{file_name}': {e}")


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    cat_file()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
