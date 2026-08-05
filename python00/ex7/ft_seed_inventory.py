def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if "packets" in unit:
        print(seed_type.capitalize(), " seeds: ", sep="", end="")
        print(quantity, "packets available")
    elif "grams" in unit:
        print(seed_type.capitalize(), " seeds: ", sep="", end="")
        print(quantity, "grams total")
    elif "area" in unit:
        print(seed_type.capitalize(), " seeds: ", sep="", end="")
        print("covers", quantity, "square meters")
    else:
        print("Unknown unit type")
