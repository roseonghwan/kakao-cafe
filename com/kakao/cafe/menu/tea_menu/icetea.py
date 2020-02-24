from com.kakao.cafe.menu.tea_menu.tea import Tea


class IceTea(Tea):
    def __init__(self):
        super().__init__()
        self.__peachPowder = 1
        self.name = "IceTea"
        self.__price = 3000
        self.__water = 300

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int) -> None:
        self.__price = price

    def getWater(self) -> int:
        return self.__water

    def setWater(self, water: int) -> None:
        self.__water = water

    def isIced(self) -> bool:
        return True

    def setIced(self, iced: bool) -> None:
        pass

    def getpeachPowder(self) -> int:
        return self.__peachPowder

    def setpeachPowder(self, peachPowder: int) -> None:
        self.__peachPowder = peachPowder

    def addPeachPowder(self, amount: int) -> None:
        self.setpeachPowder(self.getpeachPowder() + amount)
        self.setPrice(self.getPrice() + amount * 400)
