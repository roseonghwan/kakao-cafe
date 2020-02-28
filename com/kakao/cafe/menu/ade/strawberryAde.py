from com.kakao.cafe.menu.ade.ade import Ade
from abc import ABCMeta, abstractmethod


class StrawberryAde(Ade, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.__strawberry = 1
        self.name = 'StrawberryAde'
        self.__price = 3500
        self.__soda = 300
        self._iced = True

    def getName(self) -> str:
        return self.name

    def setName(self, name) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price) -> None:
        self.__price = price

    def isIced(self) -> bool:
        try:
            if self._iced == True:
                return self._iced
            else:
                raise AttributeError

        except AttributeError:
            print("에이드는 뜨겁게 드실 수 없습니다.")

    def setIced(self, _iced) -> None:
        pass

    def getSoda(self) -> None:
        return self.__soda

    def setSoda(self, soda: int) -> None:
        self.__soda = soda

    def getStrawberry(self) -> int:
        return self.__strawberry

    def setStrawberry(self, strawberry: int) -> None:
        self.__strawberry = strawberry

    def addStrawberry(self, amount: int) -> None:
        self.setStrawberry(self.getStrawberry() + amount)
        self.setPrice(self.getPrice() + amount * 500)
