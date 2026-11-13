from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy, DefensiveStrategy,
                 AggressiveStrategy, InvalidAction)


def battle(competitors: list[tuple[CreatureFactory, BattleStrategy]]) -> None:

    print("*** Tournament ***")
    size: int = len(competitors)
    print(f"{size} opponents involved")
    for j in range(size):
        for i in range(j + 1, size):
            f1, s1 = competitors[j]
            f2, s2 = competitors[i]
            oppo1 = f1.create_base()
            oppo2 = f2.create_base()
            print("\n* Battle *")
            print(oppo1.describe())
            print(" vs.")
            print(oppo2.describe())
            print("now fight!")
            try:
                for result in s1.act(oppo1):
                    print(result)
                for result in s2.act(oppo2):
                    print(result)
            except InvalidAction as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (healing, defensive)])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (healing, defensive)])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(aqua, normal), (healing, defensive),
            (transform, aggressive)])


if __name__ == "__main__":
    main()
