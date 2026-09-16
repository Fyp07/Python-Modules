class Plant():
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 0) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._growth_rate: float = growth_rate
        self._total_growth: float = 0

    def grow(self) -> None:
        self._height += self._growth_rate
        self._total_growth += self._growth_rate

    def age(self) -> None:
        self._age += 1

    def set_height(self, new_value: float) -> None:
        if new_value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_value
            print(f"Height updated: {self._height}cm")

    def set_age(self, new_value: int) -> None:
        if new_value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_value
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


def main() -> None:
    rose = Plant("Rose", 15, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-304)
    rose.set_age(-50)
    print()
    print(f"Current state: {rose._name}: {rose.get_height():.1f}cm, "
          f"{rose.get_age()} days old")


if __name__ == "__main__":
    main()
