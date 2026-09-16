
import typing
import sys


def read_text() -> None:
    file: typing.Optional[typing.IO] = None

    try:
        if len(sys.argv) != 2:
            print("Usage: ft_ancient_text.py <file>")
            return

        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1])
        content: str = file.read()
        print("---\n")
        print(content)
        print("\n---")

    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if file is not None and not file.closed:
            file.close()
            print(f"File '{file.name}' closed.")


def main() -> None:
    read_text()


if __name__ == "__main__":
    main()
