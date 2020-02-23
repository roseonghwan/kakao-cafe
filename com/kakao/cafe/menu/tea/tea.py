from com.kakao.cafe.menu.cafeMenu import CafeMenu


class Tea(CafeMenu):
    def __init__(self):
        super().__init__()
        self.__water = 0

    @abstractmethod
    def getWater(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def setWater(self, water: int) -> None:
        raise NotImplementedError
