#!/usr/bin/env python3

import random

achievements = ['Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme', 'Untouchable', 'Boss Slayer','Strategist', 'Speed Runner', 'Survivor', 'Treasure Hunter', 'Unstoppable', 'Hidden Path Finder', 'First Steps', 'Sharp Mind']
player = ['Alice', 'Bob', 'Charlie', 'Dylan']

def gen_player_achievements() -> set{str:}:
    for name in player:
         = set(random.sample(achievements)) #変数はどのように指定したらいいの？
        print(f"Player {name}: {}")#各setの内容を出力



if __name__ = "__main__":
    main()
