def ft_count_harvest_recursive():
    total = int(input("Days until harvest: "))
    x = 1
    def countdown_day(x, total):
        if x > total:
            return
        print("Day ", x)
        countdown_day(x + 1, total)

    countdown_day(x,total)
    print("Harvest time!")

ft_count_harvest_recursive()
