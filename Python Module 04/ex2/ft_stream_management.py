
import typing
import sys


def transform_data(content) -> None:
    file: typing.Optional[typing.IO] = None

    try:

        if len(sys.argv) != 2:
            print("Usage: ft_ancient_text.py <file>")
            return

        print("\nTransform data:")
        new_content: str = ""
        for char in content:
            if char == '\n':
                new_content += "#\n"
            else:
                new_content += char
        if content != "" and content[-1] != "\n":
            new_content += "#"

        print("---\n")
        print(new_content)
        print("\n---")

        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        file_name: str = sys.stdin.readline().strip("\n")
        if file_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{file_name}'")
            current_file = file_name
            file = open(current_file, "w")
            file.write(new_content)
            file.close()
            print(f"Data saved in file '{file_name}'")

    except FileNotFoundError as e:
        print(f"[STDERR] Error opening file "
              f"'{current_file}': {e}", file=sys.stderr)
        print("Data not saved.")
    except PermissionError as e:
        print(f"[STDERR] Error opening file "
              f"'{current_file}': {e}", file=sys.stderr)
        print("Data not saved.")
    finally:
        if file is not None and not file.closed:
            file.close()
            print(f"File '{file.name}' closed.")


def read_text() -> None:
    file: typing.Optional[typing.IO] = None

    try:
        if len(sys.argv) != 2:
            print("Usage: ft_ancient_text.py <file>")
            return

        print(f"Accessing file '{sys.argv[1]}'")

        current_file: str = sys.argv[1]
        file = open(sys.argv[1])
        content: str = file.read()

        print("---\n")
        print(content)
        print("\n---")

        if file is not None and not file.closed:
            file.close()
            print(f"File '{file.name}' closed.")

        transform_data(content)

    except FileNotFoundError as e:
        print(f"[STDERR] Error opening file "
              f"'{current_file}': {e}", file=sys.stderr)
    except PermissionError as e:
        print(f"[STDERR] Error opening file "
              f"'{current_file}': {e}", file=sys.stderr)
        print("Data not saved.")
    finally:
        if file is not None and not file.closed:
            file.close()
            print(f"File '{file.name}' closed.")


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    read_text()


if __name__ == "__main__":
    main()
