
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        67 / 0
    elif operation_number == 2:
        open("text.txt")
    elif operation_number == 3:
        "abc" + 2
    else:
        return


def test_error_types() -> None:
    for i in range(0, 5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        except ZeroDivisionError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        except FileNotFoundError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        except TypeError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("\nAll error types tested successfully!")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()


if __name__ == "__main__":
    main()
