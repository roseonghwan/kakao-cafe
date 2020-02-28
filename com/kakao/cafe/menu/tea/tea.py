from com.kakao.cafe.menu.cafeMenu import CafeMenu
from abc import ABCMeta, abstractmethod


class Tea(CafeMenu, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.__water = 0

    @abstractmethod
    def getWater(self) -> int:
        raise NotImplementedError('Method getWater not implemented')

    @abstractmethod
    def setWater(self, water: int) -> None:
        raise NotImplementedError('Method setWater not implemented')