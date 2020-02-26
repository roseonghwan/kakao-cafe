class OrangeAde(Ade):
    def __init__(self):
        super().__init__()
        self.orange = 1
        self.name = OrangeAde
        self.price = 3500
        self.soda = 300

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getPrice(self) -> int:
        return self.price

    def setPrice(self, age: int) -> None:
        self.price = price

    def isIced(self, isIced: bool) -> None:
        self.isIced = True
    
    def setIced(self) -> None:
        pass

    def getSoda(self) -> int:
        return self.soda

    def setSoda(self, soda: int) -> None:
        self.soda = soda
    
    def getOrange(self) -> int:
        return self.orange

    def setOrange(self, strawberry: int) -> None:
        self.orange = orange

    def addOrange(self, amount: int) -> None:
        self.amount = amount
        return price + amount * 500

