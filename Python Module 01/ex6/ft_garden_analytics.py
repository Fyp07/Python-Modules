class Plant():
    class Stats():
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def count_grow(self) -> None:
            self._grow_calls += 1

        def count_age(self) -> None:
            self._age_calls += 1

        def count_show(self) -> None:
            self._show_calls += 1

        def display_calls(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age,"
                  f" {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 0) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._growth_rate: float = growth_rate
        self._stats: Plant.Stats = Plant.Stats()

    def grow(self) -> None:
        self._height += self._growth_rate
        self._stats.count_grow()

    def age(self) -> None:
        self._age += 1
        self._stats.count_age()

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

    @staticmethod
    def is_older(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, "
              f"{self._age} days old")
        self._stats.count_show()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, growth_rate: float,
                 color: str, isBloom: bool = False) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._isBloom = isBloom

    def bloom(self) -> None:
        if self._isBloom is not True:
            self._isBloom = True
        print(f"[asking the {self._name} to grow and bloom]")
        self.grow()

    def grow_age_bloom(self) -> None:
        print(f"[make {self._name} grow, age and bloom]")
        if self._isBloom is not True:
            self._isBloom = True
        self.grow()
        self.age()

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._isBloom is not True:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, growth_rate: float,
                 color: str, seeds: int = 0) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def seed_grow(self) -> None:
        super().grow_age_bloom()
        self._seeds += 42


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 0, trunk_diameter: float = 0) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter = trunk_diameter
        self._shade_count = 0

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}cm"
              f" long and {self._trunk_diameter:.1f}cm wide.")
        self._shade_count += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    def display_shade(self) -> None:
        print(f"{self._shade_count} shade")


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


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.display_calls()


def main() -> None:
    rose = Flower("Rose", 15, 10, 8, "red")
    oak = Tree("Oak", 200, 365, 0, 5)
    sunflower = Seed("Sunflower", 80, 45, 15.0, "yellow")
    unkown = Plant.anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year?"
          f" -> {rose.is_older(30)}")
    print(f"Is 400 days more than a year?"
          f" -> {rose.is_older(400)}")
    print()
    print("=== Flower")
    rose.show()
    display_statistics(rose)
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print()
    print("=== Tree")
    oak.show()
    display_statistics(oak)
    oak.display_shade()
    oak.produce_shade()
    display_statistics(oak)
    oak.display_shade()
    print()
    print("=== Seed")
    sunflower.show()
    sunflower.seed_grow()
    sunflower.show()
    display_statistics(sunflower)
    print()

    print("=== Anonymous")
    unkown.show()
    display_statistics(unkown)


if __name__ == "__main__":
    main()
