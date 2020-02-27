from com.kakao.cafe.menu.ade.ade import Ade
from abc import ABCMeta, abstractmethod


class OrangeAde(Ade, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.__orange = 1
        self.name = 'OrangeAde'
        self.__price = 3500
        self.__soda = 300

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int) -> None:
        self.__price = price

    def isIced(self) -> bool:
        self._iced = True
        return self._iced

    def setIced(self, iced: bool) -> None:
        pass

    def getSoda(self) -> int:
        return self.__soda

    def setSoda(self, soda: int) -> None:
        self.__soda = soda

    def getOrange(self) -> int:
        return self.__orange

    def setOrange(self, orange: int) -> None:
        self.__orange = orange

    def addOrange(self, amount: int) -> None:
        self.setOrange(self.getOrange() + amount)
        self.setPrice(self.getPrice() + amount * 500)
