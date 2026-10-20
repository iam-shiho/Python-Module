import alchemy.grimoire.dark_spell_record

def main() -> None:
    print(
        "=== Kaboom 1 ===\n"
        "Access to alchemy/grimoire/dark_spellbook.py directly\n"
        "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION\n"
        f"{alchemy.grimoire.dark_spell_record('Fantasy', 'Earth, wind and fire')}\n"
    )

if __name__ == "__main__":
    main()
