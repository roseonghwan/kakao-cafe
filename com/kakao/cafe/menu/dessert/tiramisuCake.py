from com.kakao.cafe.menu.dessert.dessert import Dessert
from abc import ABCMeta, abstractmethod


class TiramisuCake(Dessert, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.__mascapone = 2
        self.__chocolatePowder = 1
        self.name = 'TiramisuCake'
        self.__price = 5500
        self._iced = True

    def getName(self) -> str:
        return self.name

    def setName(self, name) -> None:
        self.name = name
        return

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price) -> None:
        self.__price = price
        return

    def isIced(self) -> bool:
        return self._iced

    def setIced(self) -> None:
        pass

    def getMascapone(self) -> int:
        return self.__mascapone

    def setMascapone(self, mascapone) -> None:
        self.__mascapone = mascapone
        return

    def getChocolatePowder(self) -> int:
        return self.__chocolatePowder

    def setChocolatePowder(self, chocolatePowder) -> None:
        self.__chocolatePowder = chocolatePowder
        return

    def isMelted(self) -> bool:
        self._melted = False
        return self._melted

    def melt(self) -> bool:
        self._melted = True
        return self._melted

    def addChocolatePowder(self, amount: int) -> None:
        self.setChocolatePowder(self.getChocolatePowder() + amount)
        return
