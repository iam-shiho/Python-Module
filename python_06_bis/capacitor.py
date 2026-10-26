from ex3 import TransformCreatureFactory, TransformCapability, Creature, CreatureFactory

def testing_transform() -> None:
    transform = TransformCreatureFactory()
    base = transform.create_base()
    evolved = transform.create_evolved()

    print(
        "Testing Creature with transform capability",
        " base:",
        base.describe(),
        base.attack(),
        base.transform,
        base.attack(),
        base.revert(),
        sep="\n"
    )

    print(
        " evolved:",
        evolved.describe(),
        evolved.attack(),
        evolved.transform,
        evolved.attack(),
        evolved.revert(),
        sep="\n"
    )

if __name__ == "__main__":
    testing_transform()
