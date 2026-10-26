import typing
from abc import ABC, abstractmethod
from .creature import Flameling, Pyrodon
from .transform import Shiftling, Morphagon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> typing.Any:
        pass

    @abstractmethod
    def create_evolved(self) -> typing.Any:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> typing.Any:
        return Flameling()

    def create_evolved(self) -> typing.Any:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> typing.Any:
        return Shiftling()

    def create_evolved(self) -> typing.Any:
        return Morphagon()
