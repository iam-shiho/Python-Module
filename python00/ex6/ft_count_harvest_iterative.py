def ft_count_harvest_iterative():
    x = int(input("Days until harvest: "))
    nums = range(1, x + 1)
    for n in nums:
        print("Day ", n)
    print("Harvest time!")
