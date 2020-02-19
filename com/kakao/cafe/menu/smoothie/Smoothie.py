from com.kakao.cafe.menu.cafeMenu import CafeMenu


class Smoothie(CafeMenu):
    def __init__(self):
        super().__init__()
        self.__groundIce = 0
        self._iced = True

    def getGroundIce(self) -> int:
        raise NotImplementedError

    def setGroundIce(self, groundIce) -> None:
        raise NotImplementedError
