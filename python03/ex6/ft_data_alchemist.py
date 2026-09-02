#!/usr/bin/env python3

import random

PLAYERS = [
            "Alice",
            "bob",
            "Charlie",
            "dylan",
            "Emma",
            "Gregory",
            "john",
            "kevin",
            "Liam"
            ]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {PLAYERS}")
    capitalize_name = [player.capitalize() for player in PLAYERS]
    print(f"New list with all names capitalized: "
          f"{capitalize_name}")
    capitalized = [
                    player for player in PLAYERS
                    if player == player.capitalize()
                  ]
    print(f"New list of capitalized names only: {capitalized}")
    add_score = {player: random.randint(0, 1000) for player in PLAYERS}
    print(f"Score dict: {add_score}")
    average = round(sum(add_score.values()) / len(add_score), 2)
    print(f"Score average is {average}")
    high_scores = {
                   player: score for player,
                   score in add_score.items() if score > average
                   }
    print(f"High scores: {high_scores}")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
