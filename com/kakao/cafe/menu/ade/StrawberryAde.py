from com.kakao.cafe.menu.ade.ade import Ade

class StrawberryAde(Ade):
    def __init__(self):
        super().__init__()
        self.strawberry = 1
        self.name = 'StrawberryAde'
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

    def getStrawberry(self) -> int:
        return self.strawberry

    def setStrawberry(self, strawberry: int) -> None:
        self.strawberry = strawberry

    def addStrawberry(self, amount: int) -> None:
        self.strawberry += amount
        self.price += amount * 500
        

