from abc import ABC, abstractmethod
from .creature import Creature


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.transformed = False

    def attack(self) -> str:
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.transformed = False

    def attack(self) -> str:
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return "Morphagon stabilizes its form."
