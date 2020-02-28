from com.kakao.cafe.cafeMenu import CafeMenu
from abc import ABCMeta, abstractmethod


class Dessert(CafeMenu, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self._melted = False

    @abstractmethod
    def isMelted(self) -> None:
        raise NotImplementedError('Method isMelted not implemented')

    @abstractmethod
    def melt(self) -> None:
        raise NotImplementedError('Method melt not implemented')