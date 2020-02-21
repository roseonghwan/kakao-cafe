from com.kakao.cafe.menu.espresso.latte import Latte


class Cappuccino(Latte):
    def __init__(self):
        super().__init__()
        self.__cinnamon = 1
        self.name = "Cappuccino"
        self.price = 4500
        self._Latte__milk = 250

    def getCinnamon(self) -> int:
        return self.__cinnamon

    def setCinnamon(self, cinnamon: int) -> None:
        self.__cinnamon = cinnamon

    def addCinnamon(self, amount: int) -> None:
        setCinnamon(getCinnamon() + amount)

    def subCinnamon(self) -> None:
        setCinnamon(0)
