from com.kakao.cafe.menu.ade.ade import Ade

class LemonAde(Ade):
    def __init__(self):
        super().__init__()
        self.lemon = 1
        self.name = 'LemonAde'
        self.price = 3500
        self.soda = 300

    def getName(self) -> str:
        return self.name

    def setName(self, name) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.price

    def setPrice(self, price) -> None:
        return self.price

    def isIced(self, isIced: bool) -> None:
        self.iced = True
        return self.iced
    
    def setIced(self) -> None:
        pass

    def getSoda(self) -> None:
        return self.soda

    def setSoda(self, soda: int) -> None:
        self.soda = soda

    def getLemon(self) -> int:
        return self.lemon

    def setLemon(self, Lemon: int) -> None:
        self.lemon = lemon

    def addLemon(self, amount: int) -> None:
        self.lemon += amount
        self.price += amount * 500
        

