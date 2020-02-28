from com.kakao.cafe.menu.tea.milkTea import MilkTea


class RoyalMilkTea(MilkTea):
    def __init__(self):
        super().__init__()

        self.__royalHoney = 1
        self.name = "RoyalMilkTea"
        self.__price = 5000
        self.__milk = 350
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
        return self._iced

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

    def setBlackTea(self, blackTea: int) -> None:
        self.__blackTea = blackTea

    def getRoyalHoney(self) -> int:
        return self.__royalHoney

    def setRoyalHoney(self, royalHoney: int) -> None:
        self.__royalHoney = royalHoney

    def addBlackTea(self, amount: int) -> None:
        self.setBlackTea(self.getBlackTea() + amount)
        self.setPrice(self.getPrice() + amount * 500)

    def subBlackTea(self, amount: int) -> None:
        if amount > self.__blackTea:
            raise ValueError
            print("You can't subtract more blacktea.")
        else:
            self.setBlackTea(self.getBlackTea() - amount)

    def addRoyalHoney(self, amount: int) -> None:
        self.setRoyalHoney(self.getRoyalHoney() + amount)
        self.setPrice(self.getPrice() + amount * 1000)
