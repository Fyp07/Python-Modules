class Plant():
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 0) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._growth_rate: float = growth_rate

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


def main() -> None:
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    plants = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
