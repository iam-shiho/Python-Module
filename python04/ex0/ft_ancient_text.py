#!/usr/bin/env python3

import sys


def cat_file() -> None:
    if len(sys.argv) < 2:
        raise None_value("Usage: ft_ancient_text.py <file>")
    file_name = sys.argv[1]
    is_opend: bool = False
    try:
        print(f"Accessing file '{file_name}'")
        r_file = open(file_name, 'r')
        is_opend = True
        contents = r_file.read()
        print("---\n")
        print(contents, end="")
        print("\n---")
    except FileNotFoundError as e:
        print(f"Error opening file '{file_name}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{file_name}': {e}")
    except IsADirectoryError as e:
        print(f"Error opening file '{file_name}': {e}")
    finally:
        if is_opend:
            r_file.close()
        print(f"File '{file_name}' closed.")


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    cat_file()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
