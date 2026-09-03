#!/usr/bin/env python3

import sys


class None_value(Exception):
    pass


def cat_file() -> str:
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
        return contents
    except FileNotFoundError as e:
        print(f"Error opening file '{file_name}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{file_name}': {e}")
    except IsADirectoryError as e:
        print(f"Error opening file '{file_name}': {e}")
    return ""


def save_file(contents: str) -> None:
    try:
        print("Transform data:")
        print("---")
        print()
        print(contents)
        print()
        print("---")
        new_file = input("Enter new file name (or empty):")
        if not new_file:
            raise None_value("Not saving data.")
        print(f"Saving data to '{new_file}'")
        r_newfile = open(new_file, 'w')
        print(contents, file=r_newfile)
        print(f"Data saved in file '{new_file}'.")
    except FileNotFoundError as e:
        print(f"Error opening file '{new_file}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{new_file}': {e}")
    except IsADirectoryError as e:
        print(f"Error opening file '{new_file}': {e}")
    except None_value as e:
        print(e)


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    contents = cat_file()
    print()
    save_file(contents)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
