def ft_plant_age():
    c = int(input("Enter plant age in days: "))
    if c > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
