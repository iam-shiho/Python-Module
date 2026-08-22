#!/usr/bin/env python3
import sys

def print_score() ->None:
    print("=== Player Score Analytics ===")
    program_name, *args = sys.argv
    res = []

    for val in args:
        try:
            res.append(int(val))
        except ValueError:
            print(f"Invalid parameter: {val}")
    if len(res) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        print()
        return
    print(f"Scores processed: {res}")
    print(f"Total players: {len(res)}")
    print(f"Total score: {sum(res)}")
    print(f"Average score: {sum(res) / len(res)}")
    print(f"High score: {max(res)}")
    print(f"Low score: {min(res)}")
    print(f"Score range: {max(res) - min(res)}")
    print()

if __name__ == "__main__":
    print_score()
