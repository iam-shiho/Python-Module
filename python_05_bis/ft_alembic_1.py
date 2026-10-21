import alchemy


def main() -> None:
    print(
        "=== Alembic 1 ===\n"
        "Accessing the alchemy module using 'import alchemy'\n"
        f"Testing create_air: {alchemy.create_air()}\n"
        "Now show that not all functions can be reached\n"
        "This will raise an exception!\n"
    )
    print("Testing the hidden create_earth:", end="")
    print({alchemy.create_earth()})


if __name__ == "__main__":
    main()
