from com.kakao.cafe.menu.espresso.espresso import Espresso


class Latte(Espresso):
    def __init__(self):
        super().__init__()
        self.__milk = 300
        self._water = 350
        self.name = "Latte"
        self.__price = 4000
        self.__shot = 2.0

    def getShot(self) -> float:
        return self.__shot

    def setShot(self, shot: float) -> None:
        self.__shot = shot

    def addShot(self, amount: float) -> None:
        self.setShot(self.getShot() + amount)
        self.setPrice(self.getPrice() + amount * 500)

    def getWater(self) -> int:
        return self._water

    def setWater(self, water: int) -> None:
        self._water = water

    def getPrice(self):
        return self.__price

    def setPrice(self, price: int):
        self.__price = price

    def getMilk(self) -> int:
        return self.__milk

    def setMilk(self, milk: int) -> None:
        self.__milk = milk

    def isIced(self) -> bool:
        return self._iced

    def setIced(self, iced: bool) -> None:
        self._iced = iced