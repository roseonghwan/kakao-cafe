from com.kakao.cafe.menu.dessert.dessert import Dessert


class RainbowCheeseCake(Dessert):
    def __init__(self):
        super().__init__()
        self.__mascapone = 2
        self.name = 'RainbowCheeseCake'
        self.__price = 5500
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

    def getMascapone(self) -> int:
        return self.__mascapone

    def setMascapone(self, mascapone) -> None:
        self.__mascapone = mascapone
        return

    def isMelted(self) -> bool:
        return self._melted

    def melt(self) -> bool:
        self._melted = True
        return self._melted