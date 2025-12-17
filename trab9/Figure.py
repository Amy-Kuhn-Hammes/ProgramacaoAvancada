from abc import ABC, abstractmethod
class Figure(ABC):
    @abstractmethod
    def getPoints(self):
        pass

    @abstractmethod
    def getColor(self):
        pass

    @abstractmethod
    def draw(self, img):
        pass

    