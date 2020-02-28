from com.kakao.cafe.menu.dessert.waffle import Waffle


class FruitsWaffle(Waffle):
    def __init__(self):
        super().__init__()
        self._mango = 1
        self._strawberry = 1
        self._blueberry = 1
        self.name = 'FruitsWaffle'
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

    def getMango(self) -> int:
        return self._mango

    def setMango(self, mango) -> int:
        self._mango = mango
        return

    def getStrawberry(self) -> int:
        return self._strawberry

    def setStrawberry(self, strawberry) -> int:
        self._strawberry = strawberry
        return

    def getBlueberry(self) -> int:
        return self._blueberry

    def setBlueberry(self, blueberry) -> None:
        self._blueberry = blueberry
        return

    def getnumWaffles(self) -> int:
        return self.__numWaffles

    def setnumWaffles(self, numWaffles) -> int:
        self.__numWaffles = numWaffles
        return

    def addWaffle(self, amount) -> None:
        self.setnumWaffles(self.getnumWaffles() + amount)
        self.setPrice(self.getPrice() + amount * 1000)
        return

    def addFruitsMango(self, amount) -> None:
        self.setMango(self.getMango() + amount)
        self.setPrice(self.getPrice() + amount * 1000)
        return

    def addFruitsStrawberry(self, amount) -> None:
        self.setStrawberry(self.getStrawberry() + amount)
        self.setPrice(self.getPrice() + amount * 1000)
        return

    def addFruitsBlueberry(self, amount) -> None:
        self.setBlueberry(self.getBlueberry() + amount)
        self.setPrice(self.getPrice() + amount * 1000)
        return