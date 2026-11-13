from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass", "Vine Whip")

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"

    def heal(self) -> str:
        return f"{self.name} heals itself" \
            " for a small amount"


class Bloomelle(Creature, HealCapability):

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy", "Petal Dance")

    def attack(self) -> str:
        return f"{self.name} uses {self.attack_name}!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):

    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal", "boosted strike")
        self.is_transformed: bool = False

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a {self.attack_name}!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        if self.is_transformed:
            return f"{self.name} is already transformed."
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        if not self.is_transformed:
            return f"{self.name} is not transformed."
        self.is_transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):

    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon", "morph strike")
        self.is_transformed: bool = False

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating {self.attack_name}!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        if self.is_transformed:
            return f"{self.name} is already transformed."
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        if not self.is_transformed:
            return f"{self.name} is not transformed."
        self.is_transformed = False
        return f"{self.name} stabilizes its form."
