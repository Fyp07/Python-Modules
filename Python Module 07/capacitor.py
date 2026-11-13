from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from typing import cast


def healing_test(factory: HealingCreatureFactory) -> None:

    """ Create, describe, attack and
    heal with the creatures """

    creatures = [factory.create_base(), factory.create_evolved()]

    for i, creature in enumerate(creatures):
        if i == 0:
            print(" base:")
        else:
            print(" evolved:")
        print(creature.describe())
        print(creature.attack())
        print(cast(HealCapability, creature).heal())


def transform_test(factory: TransformCreatureFactory) -> None:

    """ Create, describe, attack, transform and
    revert with the creatures """

    creatures = [factory.create_base(), factory.create_evolved()]

    for i, creature in enumerate(creatures):
        if i == 0:
            print(" base:")
        else:
            print(" evolved:")

        print(creature.describe())
        print(creature.attack())
        print(cast(TransformCapability, creature).transform())
        print(creature.attack())
        print(cast(TransformCapability, creature).revert())


def main() -> None:
    # Factories
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    healing_test(healing_factory)

    print("\nTesting Creature with transform capability")
    transform_test(transform_factory)


if __name__ == "__main__":
    main()
