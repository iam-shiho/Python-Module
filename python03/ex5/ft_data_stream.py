#!/usr/bin/env python3

import typing
import random

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release"]

def gen_event() -> typing.Generator[tuple[str,str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(events: list) -> typing.Generator[tuple[str,str], None, list[tuple[str,str]]]:
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen_obj = gen_event()
    for i in range(1000):
        player, event = next(gen_obj)
        print(f"Event {i}: Player {player} did action {event}")
    ten_events = []
    for i in range(10):
        ten_events.append(next(gen_obj))
    print(f"Built list of 10 events: {ten_events}")
    rem_event = consume_event(ten_events)
    for i in range(10):
        print(f"Got event from list: {next(rem_event)}")
        print(f"Remains in list: {ten_events}")





if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
