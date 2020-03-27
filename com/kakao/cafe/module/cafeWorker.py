from abc import ABCMeta, abstractmethod


class CafeWorker(metaclass=ABCMeta):
    @abstractmethod
    def Print(self) -> None:
        raise NotImplementedError('Method Print not implemented')
