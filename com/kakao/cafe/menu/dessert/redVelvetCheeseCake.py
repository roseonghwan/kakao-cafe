from com.kakao.cafe.menu.dessert.dessert import Dessert


class RedVelvetCheeseCake(Dessert):
    def __init__(self):
        super().__init__()
        self.__mascapone = 2
        self.__redVelevetPowder = 2
        self.name = 'RedVelvetCheeseCake'
        self.__price = 6000
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

    def getredVelvetPowder(self) -> int:
        return self.__redVelevetPowder

    def setredVelvetPowder(self, redVelevetPowder: int) -> None:
        self.__redVelevetPowder = redVelevetPowder
        return

    def isMelted(self) -> bool:
        return self._melted

    def melt(self) -> None:
        return self._iced
        pass

    def addRedVelvetPowder(self, amount: int) -> None:
        self.setredVelvetPowder(self.getredVelvetPowder() + amount)
        self.setPrice(self.getPrice() + amount * 500)
        return
