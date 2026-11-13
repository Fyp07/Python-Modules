from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str, attack: str) -> None:
        self.name: str = name
        self.type: str = type
        self.attack_name: str = attack

    def __str__(self) -> str:
        return self.name

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire", "Ember")

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water", "Water Gun")

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying", "Flamethrower")

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water", "Hydro Pump")

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"
