from com.kakao.cafe.menu.smoothie.smoothie import Smoothie


class YogurtSmoothie(Smoothie):
    def __init__(self):
        super().__init__()
        self.__yogurt = 1
        self.name = "YogurtSmoothie"
        self.__price = 5000
        self.__groundIce = 400

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int) -> None:
        self.__price = price

    def getGroundIce(self) -> None:
        return self.__groundIce

    def setGroundIce(self, groundIce: int) -> None:
        self.__groundIce = groundIce

    def isIced(self) -> bool:
        self._Iced = True
        return self._Iced

    def setIced(self) -> None:
        pass

    def getYogurt(self) -> int:
        return self.__yogurt

    def setYogurt(self, yogurt: int) -> None:
        self.__yogurt = yogurt

    def addYogurt(self, amount: int) -> None:
        self.setYogurt(self.getYogurt + amount)
        self.setPrice(self.getPrice + amount * 500)
