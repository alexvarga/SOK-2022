from abc import ABC, abstractmethod

class Source(ABC):

    @abstractmethod
    def __init__(self, name, location):
        self.name = name
        self.location = location

    @abstractmethod
    def parse(self):
        pass
