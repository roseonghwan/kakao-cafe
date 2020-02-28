from com.kakao.cafe.menu.espresso.latte import Latte


class CaramelMacchiato(Latte):
    def __init__(self):
        super().__init__()
        self.__caramelSyrup = 1
        self.name = "CaramelMacchiato"
        self.__price = 4000

    def getCaramelSyrup(self) -> int:
        return self.__caramelSyrup

    def setCaramelSyrup(self, caramelSyrup: int) -> None:
        self.__caramelSyrup = caramelSyrup

    def setPrice(self, price: int) -> None:
        self.__price = price

    def getPrice(self) -> int:
        return self.__price

    def addCaramelSyrup(self, amount: int) -> None:
        self.setCaramelSyrup(self.getCaramelSyrup() + amount)
        self.setPrice(self.getPrice() + amount * 200)
