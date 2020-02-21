from com.kakao.cafe.menu.espresso.latte import Latte


class CaramelMacchiato(Latte):
    def __init__(self):
        super().__init__()
        self.__caramelSyrup = 1
        self.name = "CaramelMacchiato"
        self.price = 4000

    def getCaramelSyrup(self) -> int:
        return self.__caramelSyrup

    def setCaramelSyrup(self, caramelSyrup: int) -> None:
        self.__caramelSyrup = caramelSyrup

    def setPrice(self, price: int) -> None:
        self.price = price

    def getPrice(self) -> int:
        return self.price

    def addCaramelSyrup(self, amount: int) -> None:
        setCaramelSyrup(getCaramelSyrup() + amount)
        setPrice(getPrice() + amount * 200)
