from com.kakao.cafe.module.menuPrinter import MenuPrinter
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
from com.kakao.cafe.module.cafeWorker import CafeWorker
import unittest
from unittest.mock import patch
import io


class TestModule(unittest.TestCase):
    def setUp(self):
        # getter들의 assertEqual을 비교할 self.a를 dict 형태로 선언
        self.a = {
            'Espresso': [
                Espresso(),
                Americano(),
                Latte(),
                GreenTeaLatte(),
                VanillaLatte(),
                CafeMocha(),
                Cappuccino(),
                CaramelMacchiato()
            ],
            'Ade': [LemonAde(), OrangeAde(),
                    StrawberryAde()],
            'Smoothie':
            [YogurtSmoothie(),
             BerryBerrySmoothie(),
             PineappleSmoothie()],
            'Tea': [
                ChamomileTea(),
                GreenTea(),
                HibiscusTea(),
                IceTea(),
                LavenderTea(),
                RoyalMilkTea(),
                MatchaMilkTea(),
                PeppermintTea(),
                RooibosTea()
            ],
            'Dessert': [
                BelgianWaffle(),
                FruitsWaffle(),
                IceWaffle(),
                NewYorkCheeseCake(),
                RainbowCheeseCake(),
                RedVelvetCheeseCake(),
                TiramisuCake()
            ]
        }
        self.menuList = MenuPrinter()  # getter 테스트하는 MenuPrinter() 객체 선언

        try:
            self.impossible = CafeWorker()  # 추상클래스 Cafeworker 예외처리

        except TypeError as TE:
            self.impossible = TE.__str__()

    # cafeWorker.py의 객체가 생성되는지 테스트..
    def testCafeWorker_Instantiation(self):
        self.assertEqual(
            self.impossible,
            "Can't instantiate abstract class CafeWorker with abstract methods Print"
        )

    # menuPrinter.py에 있는 getMenuList method를 테스트..
    def testMenuPrinter_GetMenuList(self):
        self.assertEqual(len(self.menuList.getMenulist()), len(self.a))
        for i in self.menuList.getMenulist().keys():
            for j in range(len(self.menuList.getMenulist()[i])):
                self.assertEqual(self.menuList.getMenulist()[i][j].getName(),
                                 self.a[i][j].getName())
                self.assertEqual(self.menuList.getMenulist()[i][j].getPrice(),
                                 self.a[i][j].getPrice())

    # menuPrinter.py에 있는 getEspresso method를 테스트..
    def testMenuPrinter_GetEspresso(self):
        for i in range(len(self.a['Espresso'])):
            self.assertEqual(self.a['Espresso'][i].getName(),
                             self.menuList.getEspresso()[i].getName())
            self.assertEqual(self.a['Espresso'][i].getPrice(),
                             self.menuList.getEspresso()[i].getPrice())

    # menuPrinter.py에 있는 getAde method를 테스트..
    def testMenuPrinter_GetAde(self):
        for i in range(len(self.a['Ade'])):
            self.assertEqual(self.a['Ade'][i].getName(),
                             self.menuList.getAde()[i].getName())
            self.assertEqual(self.a['Ade'][i].getPrice(),
                             self.menuList.getAde()[i].getPrice())

    # menuPrinter.py에 있는 getSmoothie method를 테스트..
    def testMenuPrinter_GetSmoothie(self):
        for i in range(len(self.a['Smoothie'])):
            self.assertEqual(self.a['Smoothie'][i].getName(),
                             self.menuList.getSmoothie()[i].getName())
            self.assertEqual(self.a['Smoothie'][i].getPrice(),
                             self.menuList.getSmoothie()[i].getPrice())

    # menuPrinter.py에 있는 geTeat method를 테스트..
    def testMeunuPrinter_GetTea(self):
        for i in range(len(self.a['Tea'])):
            self.assertEqual(self.a['Tea'][i].getName(),
                             self.menuList.getTea()[i].getName())
            self.assertEqual(self.a['Tea'][i].getPrice(),
                             self.menuList.getTea()[i].getPrice())

    # menuPrinter.py에 있는 getDessert method를 테스트..
    def testMenuPrinter_GetDessert(self):
        for i in range(len(self.a['Dessert'])):
            self.assertEqual(self.a['Dessert'][i].getName(),
                             self.menuList.getDessert()[i].getName())
            self.assertEqual(self.a['Dessert'][i].getPrice(),
                             self.menuList.getDessert()[i].getPrice())


if __name__ == '__main__':
    unittest.main()
