from com.kakao.cafe.cafemenu import CafeMenu


class Dessert(CafeMenu):
    def __init__(self):
        super().__init__()
        self._melted = False

    @abstractmethod
    def melt(self) -> None:
        raise NotImplementedError('Method melt not implemented')