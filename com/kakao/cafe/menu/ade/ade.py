from com.kakao.cafe.menu.cafeMenu import CafeMenu


class Ade(CafeMenu):
    def __init__(self):
        super().__init__()
        self.__soda = 0

    def getSoda(self) -> int:
        raise NotImplementedError

    def setSoda(self, soda: int) -> None:
        raise NotImplementedError
