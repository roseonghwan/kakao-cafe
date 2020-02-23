from abc import *


class CafeMenu(metaclass=ABCMeta):
    def __init__(self):
        self.name = ""
        self.__price = 0
        self._iced = False

    @abstractmethod
    def getName(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def setName(self, name: str) -> None:
        raise NotImplementedError

    @abstractclassmethod
    def getPrice(cls, self) -> int:
        raise NotImplementedError

    @abstractclassmethod
    def setPrice(cls, self, price: int) -> None:
        raise NotImplementedError

    @abstractclassmethod
    def isIced(cls, self) -> bool:
        raise NotImplementedError

    @abstractclassmethod
    def setIced(cls, self, iced: bool) -> None:
        raise NotImplementedError