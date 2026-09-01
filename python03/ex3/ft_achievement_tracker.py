#!/usr/bin/env python3

import random

ACHIEVEMENTS = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',\
                'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps',\
                'Collector Supreme','Untouchable', 'Sharp Mind', 'Boss Slayer']

PLAYERS = ['Alice', 'Bob', 'Charlie', 'Dylan']

def gen_player_achievements() -> set[str]:
    i = random.randint(5,9)
    achieves = random.sample(ACHIEVEMENTS, i)
    return set(achieves)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    player_achieve = {}
    for name in PLAYERS:
        player_achieve[name] = gen_player_achievements()
        print(f'Player {name}: {player_achieve.get(name)}')

    print()
    print(f"All distinct achievements: {ACHIEVEMENTS}")

    print()
    sets = list(player_achieve.values())
    common = sets[0].intersection(*sets[1:])
    print(f"Common achievements: {common}")

    print()
    for name in PLAYERS:
        other_sets = []
        for other_name in PLAYERS:
            if not other_name == name:
                other_sets = other_sets + [player_achieve.get(other_name)]
        only = player_achieve.get(name).difference(*other_sets)
        print(f"Only {name} has: {only}")

    print()
    for name in PLAYERS:
        achieves = set(ACHIEVEMENTS)
        missing = achieves.difference(player_achieve.get(name))
        print(f"{name} is missing: {missing}")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
