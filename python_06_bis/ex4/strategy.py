import typing
from abc import abstractmethod, ABC
from ex3 import Creature, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: typing.Any) -> bool:
        pass

    @abstractmethod
    def act(self, creature: typing.Any) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: typing.Any) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: typing.Any) -> list[str]:
        if not self.is_valid(creature):
            raise ValueError(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature}' for this aggressive strategy"
            )
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: typing.Any) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: typing.Any) -> list[str]:
        if not self.is_valid(creature):
            raise ValueError(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.__class__.__name__}' "
                "for this aggressive strategy"
            )
        return [creature.transform(), creature.attack(), creature.revert()]
