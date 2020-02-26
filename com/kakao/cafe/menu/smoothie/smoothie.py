from com.kakao.cafe.menu.CafeMenu import CafeMenu
from abc import ABCMeta, abstractmethod


class Smoothie(CafeMenu, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.__groundIce = 0
        self._iced = True

    @abstractmethod
    def getGroundIce(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def setGroundIce(self, groundIce: int) -> int:
        raise NotImplementedError
