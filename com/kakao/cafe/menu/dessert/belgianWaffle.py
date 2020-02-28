from com.kakao.cafe.menu.dessert.waffle import Waffle
from abc import ABCMeta, abstractmethod


class BelgianWaffle(Waffle, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.__mapleSyrup = 1
        self.name = 'BelgianWaffle'
        self.__price = 5000
        self.iced = True
        self.__numWaffles = 2

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

    def isMelted(self) -> bool:
        return self._melted

    def melt(self) -> bool:
        self._melted = True
        return

    def getnumWaffles(self) -> int:
        return self.__numWaffles

    def setnumWaffles(self, numWaffles) -> int:
        self.__numWaffles = numWaffles
        return

    def addWaffle(self, amount: int) -> None:
        self.setnumWaffles(self.getnumWaffles() + amount)
        self.setPrice(self.getPrice() + (amount * 1000))
        return
