#!/usr/bin/env python3

from sys import argv

def print_command() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {argv[0]}")
    if(len(argv) > 1):
        print(f"Arguments received: {len(argv) - 1}")
        i = 1
        while(i < len(argv)):
            print(f"Argument {i}: {argv[i]}")
            i += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(argv)}")

if __name__ == "__main__":
    print_command()
