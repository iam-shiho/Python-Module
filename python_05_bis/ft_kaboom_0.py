from alchemy.grimoire import light_spell_record

def main() -> None:
    print(
        "=== Kaboom 0 ===\n"
        "Using grimoire module directly\n"
        f"Testing record light spell: {light_spell_record('Fantasy', 'Earth, wind and fire')}\n"
    )

if __name__ == "__main__":
    main()
