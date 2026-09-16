
import sys


def player_analytics() -> None:
    print("=" * 40)
    print(f"{'Player Score Analytics':^40}")
    print("=" * 40)

    if len(sys.argv) >= 2:
        scores: list = []
        for score in sys.argv[1:]:
            try:
                scores.append(int(score))
            except ValueError:
                print(f"\nError: The argument '{score}' is not a number.")
        if not scores:
            print("No valid arguments provided "
                  f"by the user: {sys.argv}")
            print("Usage: <score1> <score2> ...")
            return

        players: int = len(scores)
        total_score: int = sum(scores)
        avarage_score: float = total_score / players
        highest_score: int = max(scores)
        lowest_score: int = min(scores)
        score_range: int = highest_score - lowest_score

        print(f"\nScores processed: {scores}\n")
        print(f"{'-' * 15} Statistics {'-' * 15}")
        print(f"{'Total players:':<35} {players}")
        print(f"{'Total score:':<35} {total_score}")
        print(f"{'Avarage score:':<35} {avarage_score:.2f}")
        print(f"{'Highest score:':<35} {highest_score}")
        print(f"{'Lowest score:':<35} {lowest_score}")
        print(f"{'Score range:':<35} {score_range}")
        print("-" * 42)

    else:
        print("No arguments provided by the user. "
              "Usage: <score1> <score2> ...")


def main() -> None:
    player_analytics()


if __name__ == "__main__":
    main()
