from com.kakao.cafe.menu.espresso.latte import Latte


class VanillaLatte(Latte):
    def __init__(self):
        super().__init__()
        self.__vanillaSyrup = 1
        self.name = "VanillaLatte"
        self.__price = 4000

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int) -> None:
        self.__price = price

    def getVanillaSyrup(self) -> int:
        return self.__vanillaSyrup

    def setVanillaSyrup(self, vanillaSyrup: int) -> None:
        self.__vanillaSyrup = vanillaSyrup

    def addVanillaSyrup(self, amount: int) -> None:
        setVanillaSyrup(getVanillaSyrup() + amount)
        setPrice(getPrice() + amount * 200)
