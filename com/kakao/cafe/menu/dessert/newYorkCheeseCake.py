from com.kakao.cafe.menu.dessert.dessert import Dessert


class NewYorkCheeseCake(Dessert):
    def __init__(self):
        super().__init__()
        self.__newYorkCheese = 3
        self.name = 'NewYorkCheeseCake'
        self.__price = 5000
        self._iced = True

    def getName(self) -> str:
        return self.name

    def setName(self, name) -> None:
        self.name = name
        return

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price) -> None:
        self.__price = price
        return

    def isIced(self) -> bool:
        return self._iced

    def setIced(self) -> None:
        pass

    def getnewYorkCheeseCake(self) -> int:
        return self.__newYorkCheese

    def setnewYorkCheese(self, newYorkCheese) -> None:
        self.__newYorkCheese = newYorkCheese
        return

    def isMelted(self) -> bool:
        return self._melted

    def melt(self) -> bool:
        self._melted = True
        return self._melted