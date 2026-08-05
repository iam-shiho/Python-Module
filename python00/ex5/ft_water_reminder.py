def ft_water_reminder():
    c = int(input("Days since last watering: "))
    if c >= 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
