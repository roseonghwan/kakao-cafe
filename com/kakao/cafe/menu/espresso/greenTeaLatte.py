from com.kakao.cafe.menu.espresso.latte import Latte


class GreenTeaLatte(Latte):
    def __init__(self):
        super().__init__()
        self.__greenTea = 1
        self.__condensedMilk = 1
        self.name = "GreenTeaLatte"
        self.price = 4000

    def getPrice(self) -> int:
        return self.price

    def setPrice(self, price: int) -> None:
        self.price = price

    def getGreenTea(self) -> int:
        return self.__greenTea

    def setGreenTea(self, greenTea) -> None:
        self.__greenTea = greenTea

    def addGreenTea(self, amount: int) -> None:
        setGreenTea(getGreenTea() + amount)

    def getCondensedMilk(self) -> int:
        return self.__condensedMilk

    def setCondensedMilk(self, condensedMilk: int) -> None:
        self.__condensedMilk = condensedMilk

    def addCondensedMilk(self, amount) -> None:
        setCondensedMilk(getCondensedMilk() + amount)
        setPrice(getPrice() + amount * 300)
