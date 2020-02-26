from com.kakao.cafe.menu.smoothie.smoothie import Smoothie


class PineappleSmoothie(Smoothie):
    def __init__(self):
        super().__init__()
        self.__pineapple = 1
        self.name = "PineappleSmoothie"
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

    def getPineApple(self) -> int:
        return self.__pineapple

    def setPineApple(self, pineApple: int) -> None:
        self.__pineapple = pineApple

    def addPineapple(self, amount: int) -> None:
        self.setPineApple(self.getPineApple + amount)
        self.setPrice(self.getPrice + amount * 500)
