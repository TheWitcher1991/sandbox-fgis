from abc import ABC, abstractmethod


class EngineAdapter(ABC):

    @abstractmethod
    def generate_number(self): ...

    @abstractmethod
    def validate(self): ...
