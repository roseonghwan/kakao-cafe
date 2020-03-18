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

    def testPaymentSystem_cardPay(self):  # 카드결제 테스트
        self.paymentManager.selectPaymentWay()
        self.assertEqual(self.paymentManager.getPaymentSystem(), "카드")

    def testPaymentSystem_cashPay(self):  # 현금결제 테스트
        self.paymentManager.selectPaymentWay()
        self.assertEqual(self.paymentManager.getPaymentSystem(), "현금")

    def testPaymentSystem_gifticonPay(self):  # 기프티콘 결제 테스트
        self.paymentManager.selectPaymentWay()
        self.assertEqual(self.paymentManager.getPaymentSystem(), "기프티콘")


if __name__ == '__main__':
    unittest.main()