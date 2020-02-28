from com.kakao.cafe.menu.tea.tea import Tea


class HibiscusTea(Tea):
    def __init__(self):
        super().__init__()

        self.__hibiscusTea = 1
        self.name = "HibiscusTea"
        self.__price = 3000
        self.__water = 200

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

    def getHibiscusTea(self) -> int:
        return self.__hibiscusTea

    def setHibiscusTea(self, hibiscusTea: int) -> None:
        self.__hibiscusTea = hibiscusTea

    def addHibiscusTea(self, amount: int) -> None:
        self.setHibiscusTea(self.getHibiscusTea() + amount)
        self.setPrice(self.getPrice() + amount * 500)
