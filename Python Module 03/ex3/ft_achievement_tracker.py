
import random


def gen_player_achivements(achivements: list) -> set:
    selected: list = random.sample(achivements,
                                   random.randint(1, len(achivements)))
    return set(selected)


def show_achivements(achivements: set[str]) -> None:
    count = 0

    for achivement in achivements:
        print(f"[{achivement}]", end=" ")
        count += 1
        if count == 3:
            print()
            count = 0
    print()


def show_player(player: str, achivements: set[str]) -> None:
    print("=" * 50)
    title = f"{player}'s achievements"
    print(f"{title:^50}")
    print("=" * 50)
    show_achivements(achivements)


def main() -> None:
    achivements_list: list = [
        "Crafting genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Speed Runner", "Unstoppable",
        "Treasure Hunter", "First Steps", "Survivor",
        "Sharp Mind"
    ]

    achivements: set = set(achivements_list)
    alice: set = gen_player_achivements(achivements_list)
    bob: set = gen_player_achivements(achivements_list)
    charlie: set = gen_player_achivements(achivements_list)
    dylan: set = gen_player_achivements(achivements_list)
    common: set = set.intersection(alice, bob, charlie, dylan)

    show_player("Alice", alice)
    show_player("Bob", bob)
    show_player("Charlie", charlie)
    show_player("Dylan", dylan)

    print("=" * 50)
    print(f"{'All distinct achievements':^50}")
    print("=" * 50)
    show_achivements(achivements)
    print("=" * 50)
    print(f"\nCommon achievements: {common}\n")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}\n")
    print(f"Alice is missing: {achivements.difference(alice)}")
    print(f"Bob is missing: {achivements.difference(bob)}")
    print(f"Charlie is missing: {achivements.difference(charlie)}")
    print(f"Dylan is missing: {achivements.difference(dylan)}")


if __name__ == "__main__":
    main()
