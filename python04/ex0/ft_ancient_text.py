#!/usr/bin/env python3

import sys
import typing


def read_file(file_name: str) -> typing.IO:
    return open(file_name, 'r')


def cat_file() -> None:
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
