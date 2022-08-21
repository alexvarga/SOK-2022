from abc import ABC, abstractmethod

class Visualization(ABC):

    @abstractmethod
    def __init__(self, name, location):
        self.name = name
        self.location = location

