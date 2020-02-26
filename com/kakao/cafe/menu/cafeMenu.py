from abc import *


class CafeMenu(metaclass=ABCMeta):
    def __init__(self):
        self.name = ''
        self.__price = 0
        self._iced = False

    @abstractmethod
    def getName(self) -> str:
        raise NotImplementedError('Method getName is not implemented.')

    @abstractmethod
    def setName(self, name: str) -> None:
        raise NotImplementedError('Method setName is not implemented.')

    @abstractmethod
    def getPrice(self) -> int:
        raise NotImplementedError('Method getPrice is not implemented.')

    @abstractmethod
    def setPrice(self, price: int) -> None:
        raise NotImplementedError('Method setPrice is not implemented.')

    @abstractmethod
    def isIced(self) -> bool:
        raise NotImplementedError('Method isIced is not implemented.')

    @abstractmethod
    def setIced(self) -> None:
        raise NotImplementedError('Method setIced is not implemented.')
    