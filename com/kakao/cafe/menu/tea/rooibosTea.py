from com.kakao.cafe.menu.tea.tea import Tea


class RooibosTea(Tea):
    def __init__(self):
        super().__init__()

        self.__roobibosTea = 1
        self.name = "RooibosTea"
        self.__price = 4000
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

    def getRooibosTea(self) -> int:
        return self.__roobibosTea

    def setRooibosTea(self, roobibosTea: int) -> None:
        self.__roobibosTea = roobibosTea

    def addRooibosTea(self, amount: int) -> None:
        self.setRooibosTea(self.getRooibosTea() + amount)
        self.setPrice(self.getPrice() + amount * 700)
