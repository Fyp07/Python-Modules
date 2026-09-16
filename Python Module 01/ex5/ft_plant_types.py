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

    def set_height(self, new_value: int) -> None:
        if new_value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_value
            print(f"Height updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_value: int) -> None:
        if new_value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_value
            print(f"Age updated: {self._age} days")

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, "
              f"{self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str,
                 growth_rate: float = 0, isBloom: bool = False) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._isBloom = isBloom

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        if self._isBloom is not True:
            self._isBloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._isBloom is not True:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}cm"
              f" long and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, growth_rate: float,
                 harvest_season: str, nutritional_value: float = 0) -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow_and_age(self, grow_time: float) -> None:
        print(f"[make {self._name} grow and age for {grow_time} days]")
        for i in range(1, int(grow_time) + 1):
            self.grow()
            self.age()
            self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def main() -> None:
    rose = Flower("Rose", 15, 10, "red", False)
    oak = Tree("Oak", 200, 365, 10, 5)
    tomato = Vegetable("Tomato", 5, 10, 2.1, "April")
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato.show()
    tomato.grow_and_age(20)
    tomato.show()


if __name__ == "__main__":
    main()
