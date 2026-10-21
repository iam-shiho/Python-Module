from alchemy import grimoire


def main() -> None:
    result = grimoire.light_spell_record(
        'Fantasy', 'Earth, wind and fire'
    )
    print(
        "=== Kaboom 0 ===\n"
        "Using grimoire module directly\n"
        f"Testing record light spell: {result}\n"
    )


if __name__ == "__main__":
    main()
