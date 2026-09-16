
import random


def data_alchemist() -> None:
    players: list[str] = ["Alice", "bob", "Charlie", "dylan",
                          "Emma", "Gregory", "john", "kevin", "Liam"]
    capitalized_names: list[str] = [name for name in players
                                    if name == name.capitalize()]
    all_capitalized_names: list[str] = [name.capitalize() for name in players]
    score_dict: dict[str, int] = {key.capitalize():
                                  random.randint(1, 1000) for key in players}

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_capitalized_names}")
    print(f"New list of capitalized names only: {capitalized_names}")
    print(f"Score dict: {score_dict}")

    score_avarage: float = sum(score_dict.values()) / len(players)
    print(f"Score average is {score_avarage:.2f}")

    leaderboard: dict[str, int] = {name: score for name, score in
                                   score_dict.items() if score > score_avarage}

    print(f"High scores: {leaderboard}")


def main() -> None:
    data_alchemist()


if __name__ == "__main__":
    main()
