from com.kakao.cafe.menu.smoothie.smoothie import Smoothie


class YogurtSmoothie(Smoothie):
    def __init__(self):
        super().__init__()
        self.yogurt = 1
        self.name = "YogurtSmoothie"
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

    def getYogurt(self) -> int:
        return self.yogurt

    def setYogurt(self, yogurt: int) -> None:
        self.yogurt = yogurt

    def addYogurt(self, yogurt: int) -> None:
        self.yogurt += yogurt
        self.price += yogurt * 500
