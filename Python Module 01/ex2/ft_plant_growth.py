class Plant():
    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float) -> None:
        self.name: str = name
        self.height: float = height
        self._age: int = age
        self.growth_rate: float = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")


def main() -> None:
    rose = Plant("Rose", 25, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()
    initial_height = rose.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {rose.height - initial_height:.1f}cm")


if __name__ == "__main__":
    main()
