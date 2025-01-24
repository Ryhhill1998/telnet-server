from abc import ABC, abstractmethod


class AbstractCommandProcessor(ABC):

    @abstractmethod
    def process(self, command: str) -> str:
        pass
