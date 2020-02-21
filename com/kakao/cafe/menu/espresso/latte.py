from com.kakao.cafe.menu.espresso import espresso


class Latte(espresso):
    def __init__(self):
        super().__init__()
        self.__milk = 300
        self._water = 350
        self.name = "Latte"
        self.price = 4000
        self.shot = 2.0

    def getMilk(self) -> int:
        return self.__milk

    def setMilk(self, milk: int) -> None:
        self.__milk = milk

    def isIced(self) -> bool:
        return self._iced

    def setIced(self, iced: bool) -> None:
        self._iced = iced