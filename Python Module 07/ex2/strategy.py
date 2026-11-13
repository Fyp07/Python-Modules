from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability
from typing import cast


class InvalidAction(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidAction(f"Invalid Creature '{creature}' "
                                "for this normal strategy")
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidAction(f"Invalid Creature '{creature}' "
                                "for this aggressive strategy")
        return [cast(TransformCapability, creature).transform(),
                creature.attack(),
                cast(TransformCapability, creature).revert()]


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidAction(f"Invalid Creature '{creature}' "
                                "for this defensive strategy")
        return [creature.attack(),
                cast(HealCapability, creature).heal()]
