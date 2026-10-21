def main() -> None:
    print(
        "=== Kaboom 1 ===\n"
        "Access to alchemy/grimoire/dark_spellbook.py directly\n"
        "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION\n"
    )
    import alchemy.grimoire.dark_spellbook
    result = alchemy.grimoire.dark_spell_record(
        'Fantasy', 'Earth, wind and fire'
    )
    print(f"{result}\n")


if __name__ == "__main__":
    main()
