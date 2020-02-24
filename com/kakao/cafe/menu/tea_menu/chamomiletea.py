from com.kakao.cafe.menu.tea_menu.tea import Tea


class ChamomileTea(Tea):
    def __init__(self):
        super().__init__()
        self.__chamomileTea = 1
        self.name = ChamomileTea
        self.__price = 3500
        self.__water = 400

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

    def getchamomileTea(self) -> int:
        return self.__chamomileTea

    def setchamomileTea(self, chamomileTea: int) -> None:
        self.__chamomileTea = chamomileTea

    def addChamomileTea(self, amount: int) -> None:
        self.setchamomileTea(self.getchamomileTea() + amount)
        self.setPrice(self.getPrice() + amount * 500)
