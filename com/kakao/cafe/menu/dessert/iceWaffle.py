from com.kakao.cafe.menu.dessert.waffle import Waffle


class IceWaffle(Waffle):
    def __init__(self):
        super().__init__()
        self.iceCream = 2
        self.name = 'IceWaffle'
        self.__price = 6000
        self.__numWaffles = 2

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
        self._iced = True
        return self._iced

    def setIced(self, iced: bool) -> None:
        pass

    def isMelted(self) -> bool:
        return self._melted

    def melt(self) -> bool:
        self._melted = True
        return self._melted

    def geticeCream(self) -> int:
        return self.iceCream

    def seticeCream(self, iceCream) -> None:
        self.iceCream = iceCream

    def getnumWaffles(self) -> int:
        return self.__numWaffles

    def setnumWaffles(self, numWaffles) -> None:
        self.__numWaffles = numWaffles

    def addWaffle(self, amount) -> None:
        self.setnumWaffles(self.getnumWaffles() + amount)
        self.setPrice(self.getPrice() + amount * 1000)
        return

    def addIceCream(self, amount) -> None:
        self.seticeCream(self.geticeCream() + amount)
        self.setPrice(self.getPrice() + amount * 500)
        return
