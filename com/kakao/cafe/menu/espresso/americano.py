from com.kakao.cafe.menu.espresso import espresso


class Americano(espresso):
    def __init__(self):
        super().__init__()
        self._water = 350
        self.name = "Americano"
        self.price = 3000

    def getWater(self) -> int:
        return self._water

    def setWater(self, water: int) -> None:
        self._water = water

    def isIced(self) -> bool:
        return self._iced

    def setIced(self, iced) -> None:
        self._iced = True
