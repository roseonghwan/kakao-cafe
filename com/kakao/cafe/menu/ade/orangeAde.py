from com.kakao.cafe.menu.ade import ade


class OrangeAde(ade):
    def __init__(self):
        super().__init__()
        self.__orange = 1
        self.name = "OrangeAde"
        self.price = 3500
        self.soda = 300

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.price

    def setPrice(self, price: int) -> None:
        self.price = price

    def isIced(self) -> bool:
        self.iced = True
        return self.iced

    def setIced(self, iced: bool) -> None:
        pass

    def getSoda(self) -> int:
        return self.soda

    def setSoda(self, soda: int) -> None:
        self.soda = soda

    def getOrange(self) -> int:
        return self.__orange

    def setOrange(self, orange: int) -> None:
        self.__orange = orange

    def addOrange(self, amount: int) -> None:
        setOrange(getOrange() + amount)
        setPrice(getPrice() + amount * 500)