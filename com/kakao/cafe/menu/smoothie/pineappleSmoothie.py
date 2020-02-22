from com.kakao.cafe.menu.smoothie.smoothie import Smoothie


class PineappleSmoothie(Smoothie):
    def __init__(self):
        super().__init__()
        self.pineapple = 1
        self.name = "PineappleSmoothie"
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

    def getPineApple(self) -> int:
        return self.pineapple

    def setPineApple(self, pineApple: int) -> None:
        self.pineapple = pineApple

    def addPineapple(self, pineapple: int) -> None:
        self.pineapple += pineapple
        self.price += pineapple * 500
