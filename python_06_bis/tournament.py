from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import BattleStrategy, NormalStrategy, AggressiveStrategy


def single_battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print(
        "*** Tournament ***\n"
        f"{len(opponents)} opponents involved\n"
        "\n* Battle *"
    )
    for i in range(len(opponents)):
        factory, _ = opponents[i]
        creature = factory.create_base()
        if not i == 0:
            print(" vs.")
        print(creature.describe())

    print(" now fight!")
    for factory, strategy in opponents:
        creature = factory.create_base()
        try:
            actions = strategy.act(creature)
            for action in actions:
                print(action)
        except ValueError as e:
            print(e)


def main() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    print(
        "Tournament 0 (basic)\n"
        "[ (Flameling+Normal), (Shiftling+Aggressive) ]"
    )
    single_battle([(flame, normal), (transform, aggressive)])

    print(
        "\nTournament 1 (error)\n"
        "[ (Shiftling+Aggressive), (Flameling+Aggressive) ]"
    )
    single_battle([(transform, aggressive), (flame, aggressive)])


if __name__ == "__main__":
    main()
