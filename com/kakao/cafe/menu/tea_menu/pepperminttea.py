from com.kakao.cafe.menu.tea_menu.tea import Tea


class PeppermintTea(Tea):
    def __init__(self):
        super().__init__()

        self.__peppermintTea = 1
        self.name = "PeppermintTea"
        self.__price = 3500
        self.__water = 350

        def getName(self) -> str:
            return self.name

        def setNmae(self, name: str) -> None:
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

        def getpeppermintTea(self) -> int:
            return self.__peppermintTea

        def setpeppermintTea(self, peppermintTea: int) -> None:
            self.__peppermintTea = peppermintTea

        def addPeppermintTea(self, amount: int) -> None:
            self.setpeppermintTea(self.getpeppermintTea() + amount)
            self.setPrice(self.getPrice() + amount * 500)
