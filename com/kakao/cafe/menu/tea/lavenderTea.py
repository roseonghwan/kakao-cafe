from com.kakao.cafe.menu.tea.tea import Tea


class LavenderTea(Tea):
    def __init__(self):
        super().__init__()

        self.__lavenderTea = 1
        self.name = "LavenderTea"
        self.__price = 3500
        self.__water = 300

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int) -> None:
        self.__price = price

    def isIced(self) -> bool:
        return self._iced

    def setIced(self, iced: bool) -> None:
        self._iced = iced

    def getWater(self) -> int:
        return self.__water

    def setWater(self, water: int) -> None:
        self.__water = water

    def getLavenderTea(self) -> int:
        return self.__lavenderTea

    def setLavenderTea(self, lavenderTea: int) -> None:
        self.__lavenderTea = lavenderTea

    def addLavenderTea(self, amount: int) -> None:
        self.setLavenderTea(self.getLavenderTea() + amount)
        self.setPrice(self.getPrice() + amount * 500)
