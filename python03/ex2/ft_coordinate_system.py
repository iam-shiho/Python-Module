#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        input_value = input("Enter new coordinates as floats"
                            " in format 'x,y,z': ")
        tmp = list(input_value.split(","))
        if len(tmp) != 3:
            print("Invalid syntax")
            continue
        res: list[float] = []
        try:
            for val in tmp:
                res = res + [float(val)]
            return (res[0], res[1], res[2])
        except ValueError as e:
            print(f"Error on parameter '{val}': {e}")
            continue


def coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    coordinates = math.sqrt((pos1[0])**2 + (pos1[1])**2 + (pos1[2])**2)
    print(f"Distance to center: {round(coordinates,4)}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    coordinates = math.sqrt(
                  (pos2[0] - pos1[0]) ** 2
                  + (pos2[1] - pos1[1]) ** 2
                  + (pos2[2] - pos1[2]) ** 2
    )
    print(f"Distance between the 2 sets of "
          f"coordinates: {round(coordinates,4)}")


if __name__ == '__main__':
    try:
        coordinate_system()
    except Exception as e:
        print(f"Error: {e}")
