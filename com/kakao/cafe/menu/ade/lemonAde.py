from com.kakao.cafe.menu.ade import ade


class LemonAde(ade):
    def __init__(self):
        super().__init__()
        self.__lemon = 1
        self.name = "LemonAde"
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

    def getLemon(self) -> int:
        return self.__lemon

    def setLemon(self, lemon: int) -> None:
        self.__lemon = lemon

    def addLemon(self, amount: int) -> None:
        setLemon(getLemon() + amount)
        setPrice(getPrice() + amount * 500)