from com.kakao.cafe.module.menuPrinter import MenuPrinter
from com.kakao.cafe.module.orderTaker import OrderTaker
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
        try:
            self.impossible = CafeWorker()

        except TypeError as TE:
            self.impossible = TE.__str__()

    def testOrderTaker_AddName(self):
        self.nameList = [0]
        self.nameAnswer = ['Espresso']
        with patch('builtins.input', side_effect=self.nameList):
            ans = self.orderTaker.addName(0)
        self.assertEqual(ans, self.nameAnswer)

    def testOrderTaker_AskAmount(self):
        self.amountList = [4]
        self.amountAnswer = [4]
        with patch('builtins.input', side_effect=self.amountList):
            ans = self.orderTaker.askAmount()
        self.assertEqual(ans, self.amountAnswer)

    def testOrderAddAllPrice(self):
        self.allPriceList = [0]  #0-> Espresso
        self.allPriceAnswer = 5000  #Espresso Price

        self.orderTaker.getOrderList().append('Espresso')
        self.orderTaker.getOrderList().append(2)
        with patch('builtins.input', side_effect=self.allPriceList):
            ans = self.orderTaker.addAllPrice(0)
        print(self.orderTaker.getAllPrice())
        self.assertEqual(ans, self.allPriceAnswer)

    def testOrderTaker_AskAddShot(self):
        self.addshotList = [True, True, '2']
        self.addshotAnswer = ['addShot', 2.0]
        with patch('builtins.input', side_effect=self.addshotList):
            ans = self.orderTaker.askAddshot()
        self.assertEqual(ans, self.addshotAnswer)

    def testOrderTaker_askSizeUp(self):
        self.askSizeUpList = [True, False]
        self.askSizeUpAnswer = ['sizeUp', 'Venti']
        with patch('builtins.input', side_effect=self.askSizeUpList):
            ans = self.orderTaker.askSizeUp()
        self.assertEqual(ans, self.askSizeUpAnswer)

    def testOrderTaker_askGreenTea(self):
        self.askGreenTeaList = [True, '2']
        self.askGreenTeaAnswer = ['addGreenTea', 2]
        with patch('builtins.input', side_effect=self.askGreenTeaList):
            ans = self.orderTaker.askGreenTea()
        self.assertEqual(ans, self.askGreenTeaAnswer)

    def testOrderTaker_askCondensedMilk(self):
        self.askCondensedMilkList = [True, '2']
        self.askCondensedMilkAnswer = ['addCondensedMilk', 2]
        with patch('builtins.input', side_effect=self.askCondensedMilkList):
            ans = self.orderTaker.askCondensedMilk()
        self.assertEqual(ans, self.askCondensedMilkAnswer)

    def testOrderTaker_askVanillaSyrup(self):
        self.askVanillaSyrupList = [True, '2']
        self.askVanillaSyrupAnswer = ['addVanillaSyrup', 2]
        with patch('builtins.input', side_effect=self.askVanillaSyrupList):
            ans = self.orderTaker.askVanillaSyrup()
        self.assertEqual(ans, self.askVanillaSyrupAnswer)

    def testOrderTaker_askCafeMocha(self):
        self.askCafeMochaList = [True, '2']
        self.askCafeMochaAnswer = ['addCafeMocha', 2]
        with patch('builtins.input', side_effect=self.askCafeMochaList):
            ans = self.orderTaker.askCafeMocha()
        self.assertEqual(ans, self.askCafeMochaAnswer)

    def testOrderTaker_askCinnamon(self):
        self.askCinnamonList = [True, '2']
        self.askCinnamonAnswer = ['addCinnamon', 2]
        with patch('builtins.input', side_effect=self.askCinnamonList):
            ans = self.orderTaker.askCinnamon()
        self.assertEqual(ans, self.askCinnamonAnswer)

    def testOrderTaker_askCaramelSyrup(self):
        self.askCaramelSyrupList = [True, '2']
        self.askCaramelSyrupAnswer = ['addCaramelSyrup', 2]
        with patch('builtins.input', side_effect=self.askCaramelSyrupList):
            ans = self.orderTaker.askCaramelSyrup()
        self.assertEqual(ans, self.askCaramelSyrupAnswer)

    def testOrderTaker_askLemon(self):
        self.askLemonList = [True, '2']
        self.askLemonAnswer = ['addLemon', 2]
        with patch('builtins.input', side_effect=self.askLemonList):
            ans = self.orderTaker.askLemon()
        self.assertEqual(ans, self.askLemonAnswer)

    def testOrderTaker_askOrange(self):
        self.askOrangeList = [True, '2']
        self.askOrangeAnswer = ['addOrange', 2]
        with patch('builtins.input', side_effect=self.askOrangeList):
            ans = self.orderTaker.askOrange()
        self.assertEqual(ans, self.askOrangeAnswer)

    def testOrderTaker_askStrawberry(self):
        self.askStrawberryList = [True, '2']
        self.askStrawberryAnswer = ['addStrawberry', 2]
        with patch('builtins.input', side_effect=self.askStrawberryList):
            ans = self.orderTaker.askStrawberry()
        self.assertEqual(ans, self.askStrawberryAnswer)

    def testOrderTaker_askYogurt(self):
        self.askYogurtList = [True, '2']
        self.askYogurtAnswer = ['addYogurt', 2]
        with patch('builtins.input', side_effect=self.askYogurtList):
            ans = self.orderTaker.askYogurt()
        self.assertEqual(ans, self.askYogurtAnswer)

    def testOrderTaker_askPineapple(self):
        self.askPineappleList = [True, '2']
        self.askPineappleAnswer = ['addPineapple', 2]
        with patch('builtins.input', side_effect=self.askPineappleList):
            ans = self.orderTaker.askPineapple()
        self.assertEqual(ans, self.askPineappleAnswer)

    def testOrderTaker_askChamomileTea(self):
        self.askChamomileTeaList = [True, '2']
        self.askChamomileTeaAnswer = ['addChamomileTea', 2]
        with patch('builtins.input', side_effect=self.askChamomileTeaList):
            ans = self.orderTaker.askChamomileTea()
        self.assertEqual(ans, self.askChamomileTeaAnswer)

    def testOrderTaker_askHibiscusTea(self):
        self.askHibiscusTeaList = [True, '2']
        self.askHibiscusTeaAnswer = ['addHibiscusTea', 2]
        with patch('builtins.input', side_effect=self.askHibiscusTeaList):
            ans = self.orderTaker.askHibiscusTea()
        self.assertEqual(ans, self.askHibiscusTeaAnswer)

    def testOrderTaker_askPeachPowder(self):
        self.askPeachPowderList = [True, '2']
        self.askPeachPowderAnswer = ['addPeachPowder', 2]
        with patch('builtins.input', side_effect=self.askPeachPowderList):
            ans = self.orderTaker.askPeachPowder()
        self.assertEqual(ans, self.askPeachPowderAnswer)

    def testOrderTaker_askLavenderTea(self):
        self.askLavenderTeaList = [True, '2']
        self.askLavenderTeaAnswer = ['addLavenderTea', 2]
        with patch('builtins.input', side_effect=self.askLavenderTeaList):
            ans = self.orderTaker.askLavenderTea()
        self.assertEqual(ans, self.askLavenderTeaAnswer)

    def testOrderTaker_askBlackTea(self):
        self.askBlackTeaList = [True, True, '2']
        self.askBlackTeaAnswer = ['addBlackTea', 2]
        with patch('builtins.input', side_effect=self.askBlackTeaList):
            ans = self.orderTaker.askBlackTea()
        self.assertEqual(ans, self.askBlackTeaAnswer)

    def testOrderTaker_askRoyalHoney(self):
        self.askRoyalHoneyList = [True, '2']
        self.askRoyalHoneyAnswer = ['addRoyalHoney', 2]
        with patch('builtins.input', side_effect=self.askRoyalHoneyList):
            ans = self.orderTaker.askRoyalHoney()
        self.assertEqual(ans, self.askRoyalHoneyAnswer)

    def testOrderTaker_askMatcha(self):
        self.askMatchaList = [True, '2']
        self.askMatchaAnswer = ['addMatcha', 2]
        with patch('builtins.input', side_effect=self.askMatchaList):
            ans = self.orderTaker.askMatcha()
        self.assertEqual(ans, self.askMatchaAnswer)

    def testOrderTaker_askMatcha(self):
        self.askMatchaList = [True, '2']
        self.askMatchaAnswer = ['addMatcha', 2]
        with patch('builtins.input', side_effect=self.askMatchaList):
            ans = self.orderTaker.askMatcha()
        self.assertEqual(ans, self.askMatchaAnswer)

    def testOrderTaker_askPeppermintTea(self):
        self.askPeppermintTeaList = [True, '2']
        self.askPeppermintTeaAnswer = ['addPeppermintTea', 2]
        with patch('builtins.input', side_effect=self.askPeppermintTeaList):
            ans = self.orderTaker.askPeppermintTea()
        self.assertEqual(ans, self.askPeppermintTeaAnswer)

    def testOrderTaker_askRooibosTea(self):
        self.askRooibosTeaList = [True, '2']
        self.askRooibosTeaAnswer = ['addRooibosTea', 2]
        with patch('builtins.input', side_effect=self.askRooibosTeaList):
            ans = self.orderTaker.askRooibosTea()
        self.assertEqual(ans, self.askRooibosTeaAnswer)

    def testOrderTaker_askWaffle(self):
        self.askWaffleList = [True, '2']
        self.askWaffleAnswer = ['addWaffle', 2]
        with patch('builtins.input', side_effect=self.askWaffleList):
            ans = self.orderTaker.askWaffle()
        self.assertEqual(ans, self.askWaffleAnswer)

    def testOrderTaker_askFruitsMango(self):
        self.askFruitsMangoList = [True, '2']
        self.askFruitsMangoAnswer = ['addFruitsMango', 2]
        with patch('builtins.input', side_effect=self.askFruitsMangoList):
            ans = self.orderTaker.askFruitsMango()
        self.assertEqual(ans, self.askFruitsMangoAnswer)

    def testOrderTaker_askFruitsStrawberry(self):
        self.askFruitsStrawberryList = [True, '2']
        self.askFruitsStrawberryAnswer = ['addFruitsStrawberry', 2]
        with patch('builtins.input', side_effect=self.askFruitsStrawberryList):
            ans = self.orderTaker.askFruitsStrawberry()
        self.assertEqual(ans, self.askFruitsStrawberryAnswer)

    def testOrderTaker_askFruitsBlueberry(self):
        self.askFruitsBlueberryList = [True, '2']
        self.askFruitsBlueberryAnswer = ['addFruitsBlueberry', 2]
        with patch('builtins.input', side_effect=self.askFruitsBlueberryList):
            ans = self.orderTaker.askFruitsBlueberry()
        self.assertEqual(ans, self.askFruitsBlueberryAnswer)

    def testOrderTaker_askIceCream(self):
        self.askIceCreamList = [True, '2']
        self.askIceCreamAnswer = ['addIceCream', 2]
        with patch('builtins.input', side_effect=self.askIceCreamList):
            ans = self.orderTaker.askIceCream()
        self.assertEqual(ans, self.askIceCreamAnswer)

    def testOrderTaker_askRedVelvetPowder(self):
        self.askRedVelvetPowderList = [True, '2']
        self.askRedVelvetPowderAnswer = ['addRedVelvetPowder', 2]
        with patch('builtins.input', side_effect=self.askRedVelvetPowderList):
            ans = self.orderTaker.askRedVelvetPowder()
        self.assertEqual(ans, self.askRedVelvetPowderAnswer)

    def testOrderTaker_askChocolatePowder(self):
        self.askChocolatePowderList = [True, '2']
        self.askChocolatePowderAnswer = ['addChocolatePowder', 2]
        with patch('builtins.input', side_effect=self.askChocolatePowderList):
            ans = self.orderTaker.askChocolatePowder()
        self.assertEqual(ans, self.askChocolatePowderAnswer)


if __name__ == '__main__':
    unittest.main()