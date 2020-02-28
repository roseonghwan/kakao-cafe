from com.kakao.cafe.menu.cafeMenu import CafeMenu
from abc import ABCMeta, abstractmethod


class Smoothie(CafeMenu, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.__groundIce = 0
        self._iced = True

    @abstractmethod
    def getGroundIce(self) -> int:
        raise NotImplementedError('Method getGroundIce is not implemented.')

    @abstractmethod
    def setGroundIce(self, groundIce) -> None:
        raise NotImplementedError('Method setGroundIce is not implemented.')
