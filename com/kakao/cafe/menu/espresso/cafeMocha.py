from com.kakao.cafe.menu.espresso.latte import Latte


class CafeMocha(Latte):
    def __init__(self):
        super().__init__()
        self.__mocha = 1
        self.name = "CafeMocha"
        self.__price = 4000

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int) -> None:
        self.__price = price

    def getMocha(self) -> int:
        return self.__mocha

    def setMocha(self, mocha: int) -> None:
        self.__mocha = mocha

    def addMocha(self, amount) -> None:
        self.setMocha(self.getMocha() + amount)
        self.setPrice(self.getPrice() + amount * 300)