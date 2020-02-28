from com.kakao.cafe.menu.espresso.espresso import Espresso


class Americano(Espresso):
    def __init__(self):
        super().__init__()
        self._water = 350
        self.name = "Americano"
        self.__price = 3000

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int) -> None:
        self.__price = price

    def getWater(self) -> int:
        return self._water

    def setWater(self, water: int) -> None:
        self._water = water

    def isIced(self) -> bool:
        return self._iced

    def setIced(self, iced) -> None:
        self._iced = True
