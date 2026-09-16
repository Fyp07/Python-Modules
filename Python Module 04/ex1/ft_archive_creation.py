
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

        file_name = str(input("Enter new file name (or empty): "))
        if file_name == "":
            print("Not saving data.")
        else:
            current_file: str = file_name
            file = open(file_name, "w")
            file.write(new_content)
            file.close()
            print(f"Saving data to '{file_name}'")
            print(f"Data saved in file '{file_name}'")
    except FileNotFoundError as e:
        print(f"Error opening file '{current_file}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{current_file}': {e}")
    finally:
        if file is not None and not file.closed:
            file.close()


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
        print(f"Error opening file '{current_file}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{current_file}': {e}")
    finally:
        if file is not None and not file.closed:
            file.close()


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    read_text()


if __name__ == "__main__":
    main()
