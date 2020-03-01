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
import unittest
from unittest.mock import patch
import io


class TestMenuPrinter(unittest.TestCase):
    def setUp(self):
        self.menuList = MenuPrinter()

    def testGetMenuList(self):
        a = {
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
        self.assertEqual(len(self.menuList.getMenulist()), len(a))
        for i in self.menuList.getMenulist().keys():
            for j in range(len(self.menuList.getMenulist()[i])):
                self.assertEqual(self.menuList.getMenulist()[i][j].getName(),
                                 a[i][j].getName())
                self.assertEqual(self.menuList.getMenulist()[i][j].getPrice(),
                                 a[i][j].getPrice())

    def testPrint(self):
        with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
            self.menuList.Print()
        self.assertEqual(
            fakeOutput.getvalue(),
            "Wellcome to Kakao Cafe!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n|Espresso                      |Ade                           |Smoothie                      |Tea                           |Dessert                       \n------------------------------------------------------------------------------------------------------------------------------------------------------------\n| Espresso               2500  | LemonAde               3500  | YogurtSmoothie         5000  | ChamomileTea           3500  | BelgianWaffle          5000  \n| Americano              3000  | OrangeAde              3500  | BerryBerrySmoothie     5000  | GreenTea               3000  | FruitsWaffle           6000  \n| Latte                  4000  | StrawberryAde          3500  | PineappleSmoothie      5000  | HibiscusTea            3000  | IceWaffle              6000  \n| GreenTeaLatte          4000  |                              |                              | IceTea                 3000  | NewYorkCheeseCake      5000  \n| VanillaLatte           4000  |                              |                              | LavenderTea            3500  | RainbowCheeseCake      5500  \n| CafeMocha              4000  |                              |                              | RoyalMilkTea           5000  | RedVelvetCheeseCake    6000  \n| Cappuccino             4500  |                              |                              | MatchaMilkTea          4500  | TiramisuCake           5500  \n| CaramelMacchiato       4000  |                              |                              | PeppermintTea          3500  |                              \n|                              |                              |                              | RooibosTea             4000  |                              \n"
        )


if __name__ == "__main__":
    unittest.main()