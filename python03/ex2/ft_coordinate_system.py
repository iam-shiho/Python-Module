import math

def get_player_pos() -> tuple:
    while True:
        input_value = input("Enter new coordinates as floats in format 'x,y,z': ")
        tmp = list(input_value.split(","))
        if len(tmp) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(tmp[0])
            y = float(tmp[1])
            z = float(tmp[2])
            return (x, y, z)
        except ValueError as e:
            print(f"Error on parameter : {e}") #エラーこれでいいの？
            continue

def coordinate_system()-> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    coordinates =  math.sqrt((pos1[0])**2 + (pos1[1])**2 + (pos1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(coordinates,4)}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    
    coordinates =  math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2 + (pos2[2] - pos1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(coordinates,4)}")

if __name__ == "__main__":
    coordinate_system()
