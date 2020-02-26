from com.kakao.cafe.menu.espresso.latte import Latte


class Cappuccino(Latte):
    def __init__(self):
        super().__init__()
        self.__cinnamon = 1
        self.name = "Cappuccino"
        self.__price = 4500
        self.__milk = 250

    def getMilk(self) -> int:
        return self.__milk

    def setMilk(self, milk: int) -> None:
        self.__milk = milk

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int) -> None:
        self.__price = price

    def getCinnamon(self) -> int:
        return self.__cinnamon

    def setCinnamon(self, cinnamon: int) -> None:
        self.__cinnamon = cinnamon

    def addCinnamon(self, amount: int) -> None:
        self.setCinnamon(self.getCinnamon() + amount)

    def subCinnamon(self) -> None:
        self.setCinnamon(0)
