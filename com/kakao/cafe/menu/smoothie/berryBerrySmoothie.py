from com.kakao.cafe.menu.smoothie.smoothie import Smoothie

class BerryBerrySmoothie(Smoothie):
    def __init__(self):
        super().__init__()
        self.__mixedBerry = 1
        self.name = 'BerryBerrySmoothie'
        self.__price = 5000
        self.__groundIce = 400

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name
        return

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int) -> None:
        self.__price = price
        return

    def isIced(self) -> bool:
        return True

    def setIced(self) -> None:
        return

    def getGroundIce(self) -> int:
        return self.__groundIce

    def setGroundIce(self, groundIce: int) -> None:
        self.__groundIce = groundIce
        return

    def getMixedBerry(self) -> int:
        return self.__mixedBerry

    def setMixedBerry(self, mixedBerry: int) -> None:
        self.__mixedBerry = mixedBerry
        return

    def addBerry(self, amount: int) -> None:
        self.setMixedBerry(self.getMixedBerry() + amount)
        self.setPrice(self.getPrice() + amount * 500)
        return
