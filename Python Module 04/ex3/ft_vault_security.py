
def secure_archive(file_name: str, act: str | None = None,
                   content: str | None = None) -> tuple[bool, str]:
    try:
        if act == "r":
            with open(file_name, "r") as file:
                read_content: str = file.read()
                return (True, read_content)
        elif act is None and content is None:
            with open(file_name) as file:
                read_content = file.read()
                return (True, read_content)
        elif act == "w" and content is not None:
            with open(file_name, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        else:
            raise ValueError("Invalid parameter to 'act'. eg: 'r', 'w'")
    except FileNotFoundError as e:
        return (False, f"{e}")
    except PermissionError as e:
        return (False, f"{e}")
    except ValueError as e:
        return (False, f"{e}")


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("inaccessible"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("regular"))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new file", "w", "Flamengo"))


if __name__ == "__main__":
    main()
