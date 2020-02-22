from com.kakao.cafe.menu.smoothie.smoothie import Smoothie


class BerryberrySmoothie(Smoothie):
    def __init__(self):
        super().__init__()
        self.mixedBerry = 1
        self.name = "BerryberrySmoothie"
        self.price = 5000
        self.groundIce = 400

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.price

    def setPrice(self, price: int) -> None:
        self.price = price

    def getGroundIce(self) -> None:
        return self.groundIce

    def setGroundIce(self, groundIce: int) -> None:
        self.groundIce = groundIce

    def isIced(self) -> bool:
        self.Iced = True
        return self.Iced

    def setIced(self) -> None:
        pass

    def getMixedBerry(self) -> int:
        return self.mixedBerry

    def setMixedBerry(self, mixedBerry: int) -> None:
        self.mixedBerry = mixedBerry

    def addBerry(self, mixedBerry: int) -> None:
        self.mixedBerry += mixedBerry
        self.price += mixedBerry * 500

