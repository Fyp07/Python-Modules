
import sys


def main() -> None:
    args: int = len(sys.argv)

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if (args < 2):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {args - 1}")
        for i in range(1, args):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {args}")


if __name__ == "__main__":
    main()
