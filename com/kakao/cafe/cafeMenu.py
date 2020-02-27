from abc import *


class CafeMenu(metaclass=ABCMeta):

    def __init__(self):
        self.name = ''
        self.__price = 0
        self._iced = False

    @abstractmethod
    def getName(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def setName(self, name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def getPrice(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def setPrice(self, price: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def isIced(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def setIced(self) -> None:
        raise NotImplementedError
