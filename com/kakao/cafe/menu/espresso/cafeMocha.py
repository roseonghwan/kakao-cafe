from com.kakao.cafe.menu.espresso.latte import Latte


class CafeMocha(Latte):
    def __init__(self):
        super().__init__()
        self.__mocha = 1
        self.name = "CafeMocha"
        self.price = 4000

    def getPrice(self) -> int:
        return self.price

    def setPrice(self, price: int) -> None:
        self.price = price

    def getMocha(self) -> int:
        return self.__mocha

    def setMocha(self, mocha: int) -> None:
        self.__mocha = mocha

    def addMocha(self, amount) -> None:
        setMocha(getMocha() + amount)
        setPrice(getPrice() + amount * 300)