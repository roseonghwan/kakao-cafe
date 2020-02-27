from com.kakao.cafe.menu.ade.ade import Ade
from abc import ABCMeta, abstractmethod


class LemonAde(Ade, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.__lemon = 1
        self.name = 'LemonAde'
        self.__price = 3500
        self.__soda = 300

    def getName(self) -> str:
        return self.name

    def setName(self, name) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price) -> None:
        self.__price = price

    def isIced(self) -> bool:
        self._iced = True
        return self._iced

    def setIced(self, iced: bool) -> None:
        pass

    def getSoda(self) -> None:
        return self.__soda

    def setSoda(self, soda: int) -> None:
        self.__soda = soda

    def getLemon(self) -> int:
        return self.__lemon

    def setLemon(self, lemon: int) -> None:
        self.__lemon = lemon

    def addLemon(self, amount: int) -> None:
        self.setLemon(self.getLemon() + amount)
        self.setPrice(self.getPrice() + amount * 500)
