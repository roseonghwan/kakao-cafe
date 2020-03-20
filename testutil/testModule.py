from com.kakao.cafe.module.menuPrinter import MenuPrinter
from com.kakao.cafe.module.orderTaker import OrderTaker
from com.kakao.cafe.module.paymentManager import PaymentManager
from com.kakao.cafe.module.cafeWorker import CafeWorker
from com.kakao.cafe.menu.espresso.espresso import Espresso
from com.kakao.cafe.menu.espresso.americano import Americano
from com.kakao.cafe.menu.espresso.latte import Latte
from com.kakao.cafe.menu.espresso.greenTeaLatte import GreenTeaLatte
from com.kakao.cafe.menu.espresso.vanillaLatte import VanillaLatte
from com.kakao.cafe.menu.espresso.cafeMocha import CafeMocha
from com.kakao.cafe.menu.espresso.cappuccino import Cappuccino
from com.kakao.cafe.menu.espresso.caramelMacchiato import CaramelMacchiato
from com.kakao.cafe.menu.ade.lemonAde import LemonAde
from com.kakao.cafe.menu.ade.orangeAde import OrangeAde
from com.kakao.cafe.menu.smoothie.yogurtSmoothie import YogurtSmoothie
from com.kakao.cafe.menu.smoothie.berryBerrySmoothie import BerryBerrySmoothie
from com.kakao.cafe.menu.smoothie.pineappleSmoothie import PineappleSmoothie
from com.kakao.cafe.menu.ade.strawberryAde import StrawberryAde
from com.kakao.cafe.menu.tea.chamomileTea import ChamomileTea
from com.kakao.cafe.menu.tea.greenTea import GreenTea
from com.kakao.cafe.menu.tea.hibiscusTea import HibiscusTea
from com.kakao.cafe.menu.tea.iceTea import IceTea
from com.kakao.cafe.menu.tea.lavenderTea import LavenderTea
from com.kakao.cafe.menu.tea.milkTea import MilkTea
from com.kakao.cafe.menu.tea.royalMilkTea import RoyalMilkTea
from com.kakao.cafe.menu.tea.matchaMilkTea import MatchaMilkTea
from com.kakao.cafe.menu.tea.peppermintTea import PeppermintTea
from com.kakao.cafe.menu.tea.rooibosTea import RooibosTea
from com.kakao.cafe.menu.dessert.belgianWaffle import BelgianWaffle
from com.kakao.cafe.menu.dessert.fruitsWaffle import FruitsWaffle
from com.kakao.cafe.menu.dessert.iceWaffle import IceWaffle
from com.kakao.cafe.menu.dessert.newYorkCheeseCake import NewYorkCheeseCake
from com.kakao.cafe.menu.dessert.rainbowCheeseCake import RainbowCheeseCake
from com.kakao.cafe.menu.dessert.redVelvetCheeseCake import RedVelvetCheeseCake
from com.kakao.cafe.menu.dessert.tiramisuCake import TiramisuCake

import unittest
from unittest.mock import patch

import sys
from io import StringIO


class TestModule(unittest.TestCase):
    def setUp(self):
        self.testList = list()
        self.menuPrinter = MenuPrinter()
        self.orderTaker = OrderTaker()
        self.paymentManager = PaymentManager()
        try:
            self.impossible = CafeWorker()

        except TypeError as TE:
            self.impossible = TE.__str__()

    def testCardPay(self):  # 카드결제 테스트
        self.paymentManager.setCardBalance(10000)  # 초기 카드잔액 설정
        self.paymentManager.setPoint(100)  # 초기 포인트 설정
        current_point = self.paymentManager.getPoint()  # 초기 포인트의 값을 저장
        self.orderTaker.getAddlist().append(
            'Americano')  # 예시로 Americano 1개의 가격을 가져오기 위한 설정
        self.orderTaker.getAddlist().append(1)
        self.orderTaker.addAllPrice(1)
        self.paymentManager.setTtotalPrice(3000)  # 위의 Americano 1개 가격으로 설정
        current_price = self.paymentManager.getTotalPrice(
        )  # 포인트를 사용하기 전 원래의 총 가격
        self.paymentManager.selectPaymentWay()  # 결제 시작
        self.assertEqual(self.paymentManager.getPaymentSystem(),
                         "카드")  # 카드로 결제한게 맞는지 확인
        self.assertEqual(self.paymentManager.getPoint(),
                         current_point + self.orderTaker.getAllPrice() *
                         0.03)  # 포인트를 사용하지 않고!! 적립하여 포인트 테스트
        self.assertEqual(self.paymentManager.getPoint(),
                         0)  # 포인트를 사용하여!! 포인트가 0이 되는 것을 테스트
        self.assertEqual(self.paymentManager.getTotalPrice(), current_price -
                         current_point)  # 포인트를 사용하여!! 할인된 총 가격을 테스트

    def testPaymentSystem_cashPay(self):  # 현금결제 테스트
        self.paymentManager.setCash(10000)
        current_cash = self.paymentManager.getCash()
        self.orderTaker.getAddlist().append(
            'Americano')  # 예시로 Americano 1개의 가격을 가져오기 위한 설정
        self.orderTaker.getAddlist().append(1)
        self.orderTaker.addAllPrice(1)
        self.paymentManager.setTtotalPrice(3000)
        self.paymentManager.selectPaymentWay()  # 결제 시작
        self.assertEqual(self.paymentManager.getPaymentSystem(),
                         "현금")  # 현금으로 결제한게 맞는지 확인
        self.assertEqual(self.paymentManager.getChange(), current_cash -
                         self.orderTaker.getAllPrice())  # 거스름돈이 맞는지 테스트


if __name__ == '__main__':
    unittest.main()