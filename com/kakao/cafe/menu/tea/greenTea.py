from com.kakao.cafe.menu.tea.tea import Tea


class GreenTea(Tea):
    def __init__(self):
        super().__init__()
        self.__greenTea = 1
        self.name = "GreenTea"
        self.__price = 3000
        self.__water = 200

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int):
        self.__price = price

    def isIced(self):
        return self._iced

    def setIced(self, iced):
        self._iced = iced

    def getWater(self) -> int:
        return self.__water

    def setWater(self, water: int) -> None:
        self.__water = water

    def getGreenTea(self) -> int:
        return self.__greenTea

    def setGreenTea(self, greenTea: int) -> None:
        self.__greenTea = greenTea

    def addGreenTea(self, amount: int) -> None:
        self.setGreenTea(self.getGreenTea() + amount)
        self.setPrice(self.getPrice() + amount * 500)
