#!/usr/bin/env python3
import sys
import typing

def only_open() -> typing.TextIOWrapper:
    return open(sys.argv[1], 'r')

def main() -> None:
    r_file = only_open()
    contents = r_file.read()
    print(contents)

main()
