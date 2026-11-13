from ex0 import FlameFactory, AquaFactory, CreatureFactory


def creature_test(factory: CreatureFactory) -> None:

    """ Create, describe, and
    attack with the creatures """

    creatures = [factory.create_base(), factory.create_evolved()]

    for creature in creatures:
        print(creature.describe())
        print(creature.attack())


def battle(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:

    """ Make two creatures battle. """

    creature_1 = factory_1.create_base()
    creature_2 = factory_2.create_base()

    print(f"{creature_1.describe()}\n vs.\n{creature_2.describe()}")
    print(" fight!")
    print(f"{creature_1.attack()}\n{creature_2.attack()}")


def main() -> None:
    # Factories
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    # Testing Fire Creatures
    print("Testing factory")
    creature_test(flame_factory)

    # Testing Water Creatures
    print("\nTesting factory")
    creature_test(aqua_factory)

    # Battle
    print("\nTesting battle")
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
