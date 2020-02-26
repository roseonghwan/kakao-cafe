from com.kakao.cafe.cafeMenu import CafeMenu

class Ade(CafeMenu):
    def __init__(self):
        super().__init__()
        self.__soda = 0

        @abstractmethod
        def getSoda(self) -> int:
            raise NotImplementedError

        @abstractmethod
        def setSoda(self, __soda: int) -> None:
            raise NotImplementedError