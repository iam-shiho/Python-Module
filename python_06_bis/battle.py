from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def testing_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(
        "Testing factory",
        base.describe(),
        base.attack(),
        evolved.describe(),
        evolved.attack(),
        sep="\n"
    )


def testing_battle(
    factory_1: CreatureFactory,
    factory_2: CreatureFactory
) -> None:
    base_1 = factory_1.create_base()
    base_2 = factory_2.create_base()

    print(
        "Testing battle",
        base_1.describe(),
        " vs.",
        base_2.describe(),
        " fight!",
        base_1.attack(),
        base_2.attack(),
        sep="\n"
    )


def main() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()

    testing_factory(flame)
    print()
    testing_factory(transform)

    print()
    testing_battle(flame, transform)


if __name__ == "__main__":
    main()
