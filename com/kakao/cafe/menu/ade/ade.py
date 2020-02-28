<<<<<<< HEAD
from com.kakao.cafe.cafeMenu import CafeMenu
from abc import ABCMeta, abstractmethod


class Ade(CafeMenu, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.__soda = 0

        @abstractmethod
        def getSoda(self) -> int:
            raise NotImplementedError

        @abstractmethod
        def setSoda(self, __soda: int) -> None:
            raise NotImplementedError
=======

>>>>>>> b0a0d530eb431d5399871a676b9253c996654ee0
