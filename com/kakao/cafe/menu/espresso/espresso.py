from com.kakao.cafe.menu.cafeMenu import CafeMenu


class Espresso(CafeMenu):
    def __init__(self):
        super().__init__()
        self.name = "Espresso"
        self.__price = 2500
        self._iced = False
        self.__shot = 1.0
        self.__size = 'Tall'

    def getShot(self) -> float:
        return self.__shot

    def setShot(self, shot: float) -> None:
        self.__shot = shot

    def addShot(self, amount: float) -> None:
        self.setShot(self.getShot() + amount)
        self.setPrice(self.getPrice() + amount * 500)

    def subShot(self, amount: float):

        try:
            if self.getShot() > amount:
                self.setShot(self.getShot() - amount)

            else:
                raise ArithmeticError

        except ArithmeticError:
            print("더 이상 shot을 뺄 수 없습니다.\n")

    def getSize(self) -> str:
        return self.__size

    def setSize(self, size: str) -> None:
        self.__size = size

    def sizeUp(self, size: str) -> None:

        try:
            if self.getSize() == self.__size:
                self.setSize = 'Grande'
                self.setPrice(self.getPrice() + 500)

            elif self.getSize() == 'Grande':
                self.setSize = 'Venti'
                self.setPrice(self.getPrice() + 500)

            else:
                raise ValueError

        except ValueError:
            print("더 이상 size를 올릴 수 없습니다.\n")

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name
        return

    def getPrice(self) -> int:
        return self.__price

    def setPrice(self, price: int) -> None:
        self.__price = price
        return

    def setIced(self, iced) -> None:
        raise AttributeError

    def isIced(self) -> bool:
        try:
            if self._iced == False:
                return self._iced
            else:
                raise AttributeError

        except AttributeError:
            print("죄송하지만, 에스프레소는 차갑게 드실 수 없습니다.")
            