from com.kakao.cafe.menu.CafeMenu import CafeMenu


class Smoothie(CafeMenu):
    def __init__(self):
        super().__init__
        self.groundIce = 0
        self.iced = True

    def getGroundIce(self) -> None:
        raise NotImplementedError

    def setGroundIce(self, groundIce: int) -> int:
        raise NotImplementedError
