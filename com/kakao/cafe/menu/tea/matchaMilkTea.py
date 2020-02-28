from com.kakao.cafe.menu.tea.milkTea import MilkTea


class MatchaMilkTea(MilkTea):
    def __init__(self):
        super().__init__()

        self.__matcha = 1
        self.__condensedMilk = 1
        self.name = "MatchaMilkTea"
        self.__price = 4500
        self.__milk = 400
        self.__blackTea = 2

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int) -> None:
        self.__price = price

    def isIced(self) -> bool:
        return self.iced

    def setIced(self, iced: bool) -> None:
        self._iced = iced

    def getWater(self) -> int:
        pass

    def setWater(self, water: int) -> None:
        pass

    def getMilk(self) -> int:
        return self.__milk

    def setMilk(self, milk: int) -> None:
        self.__milk = milk

    def getBlackTea(self) -> int:
        return self.__blackTea

    def setBlackTea(self, blacktea: int) -> None:
        self.__blackTea = blacktea

    def getMatcha(self) -> int:
        return self.__matcha

    def setMatcha(self, matcha: int) -> None:
        self.__matcha = matcha

    def getCondensedMilk(self) -> int:
        return self.__condensedMilk

    def setCondensedMilk(self, condensedMilk: int) -> None:
        self.__condensedMilk = condensedMilk

    def addBlackTea(self, amount: int) -> None:
        self.setBlackTea(self.getBlackTea() + amount)
        self.setPrice(self.getPrice() + amount * 500)

    def subBlackTea(self, amount: int) -> None:
        if amount > self.__blackTea:
            raise ValueError
            print("You can't subtract more blacktea.")
        else:
            self.setBlackTea(self.getBlackTea() - amount)

    def addMatcha(self, amount: int) -> None:
        self.setMatcha(self.getMatcha() + amount)
        self.setPrice(self.getPrice() + amount * 400)

    def addCondensedMilk(self, amount: int) -> None:
        self.setCondensedMilk(self.getCondensedMilk() + amount)
        self.setPrice(self.getPrice() + amount * 500)
