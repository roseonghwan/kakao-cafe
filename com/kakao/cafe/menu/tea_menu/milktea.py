from com.kakao.cafe.menu.tea_menu.tea import Tea


class MilkTea(Tea):
    def __init__(self):
        super().__init__()

        self.__milk = 0
        self.__blackTea = 0

    @abstractmethod
    def getMilk(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def setMilk(self, milk: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def getBlackTea(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def setBlackTea(self, blacktea: int) -> None:
        raise NotImplementedError
