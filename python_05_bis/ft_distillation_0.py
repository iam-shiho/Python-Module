from alchemy import strength_potion, healing_potion


def main() -> None:
    print(
        "=== Distillation 0 ===\n"
        "Direct access to alchemy/potions.py\n"
        f"Testing strength_potion: {strength_potion()}\n"
        f"Testing healing_potion: {healing_potion()}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
