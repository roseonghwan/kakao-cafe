from com.kakao.cafe.menu.dessert.dessert import Dessert


class Waffle(Dessert):
    def __init__(self):
        super().__init__()
        self.__numWaffles = 2

    def isIced(self) -> bool:
        return True

    def setIced(self) -> None:
        pass

    def getnumWaffles(self) -> int:
        raise NotImplementedError('Method getnumWaffles not implemented')

    def setnumWaffles(self, numWaffles) -> int:
        raise NotImplementedError('Method setnumWaffles not implemented')

    def addWaffle(self) -> None:
        raise NotImplementedError('Method addWaffle not implemented')