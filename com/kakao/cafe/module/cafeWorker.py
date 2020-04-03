# -*- coding: utf-8 -*-
#
# cafeWorker.py
#
# Defines Kakao cafe's worker interface.

from abc import ABCMeta, abstractmethod


class CafeWorker(metaclass=ABCMeta):
    @abstractmethod
    def Print(self) -> None:
        raise NotImplementedError('Method Print not implemented')
