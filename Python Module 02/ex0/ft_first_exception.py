
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    inputs: list[str] = ["25", "abc"]
    for i in inputs:
        print(f"Input data is '{i}'")
        try:
            temp: int = input_temperature(i)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
