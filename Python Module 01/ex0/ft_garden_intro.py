def plant_info() -> None:
    name = "Rose"
    height = 25
    age = 30
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


def main() -> None:
    print("=== Welcome to My Garden ===")
    plant_info()
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
