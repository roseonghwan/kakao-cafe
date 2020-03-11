from com.kakao.cafe.menu.dessert.dessert import Dessert
from com.kakao.cafe.menu.dessert.belgianWaffle import BelgianWaffle
from com.kakao.cafe.menu.dessert.fruitsWaffle import FruitsWaffle
from com.kakao.cafe.menu.dessert.iceWaffle import IceWaffle
from com.kakao.cafe.menu.dessert.newYorkCheeseCake import NewYorkCheeseCake
from com.kakao.cafe.menu.dessert.rainbowCheeseCake import RainbowCheeseCake
from com.kakao.cafe.menu.dessert.redVelvetCheeseCake import RedVelvetCheeseCake
from com.kakao.cafe.menu.dessert.tiramisuCake import TiramisuCake
from com.kakao.cafe.menu.dessert.waffle import Waffle
from random import randint
import unittest


class TestDessert(unittest.TestCase):
    def setUp(self):
        self.belgianWaffle = BelgianWaffle()
        self.fruitsWaffle = FruitsWaffle()
        self.iceWaffle = IceWaffle()
        self.newYorkCheeseCake = NewYorkCheeseCake()
        self.rainbowCheeseCake = RainbowCheeseCake()
        self.redVelvetCheeseCake = RedVelvetCheeseCake()
        self.tiramisuCake = TiramisuCake()

    def testBelgianWaffle(self):
        self.assertEqual(self.belgianWaffle.getName(), 'BelgianWaffle')
        self.assertEqual(self.belgianWaffle.getPrice(), 5000)
        self.assertEqual(self.belgianWaffle.isMelted(), False)
        self.assertEqual(self.belgianWaffle.melt(), None)
        self.assertEqual(self.belgianWaffle.getnumWaffles(), 2)
        ComparePrice = self.belgianWaffle.getPrice()
        CompareWaffle = self.belgianWaffle.getnumWaffles()
        amount = randint(1, 5)
        self.belgianWaffle.addWaffle(amount)
        self.assertEqual(self.belgianWaffle.getnumWaffles(),
                         CompareWaffle + amount)
        self.assertEqual(self.belgianWaffle.getPrice(),
                         ComparePrice + amount * 1000)

    def testNewYorkCheeseCake(self):
        self.assertEqual(self.newYorkCheeseCake.getName(), 'NewYorkCheeseCake')
        self.assertEqual(self.newYorkCheeseCake.getPrice(), 5000)
        self.assertEqual(self.newYorkCheeseCake.isIced(), True)
        self.assertEqual(self.newYorkCheeseCake.isMelted(), False)
        self.assertEqual(self.newYorkCheeseCake.getnewYorkCheeseCake(), 3)
        self.assertEqual(self.newYorkCheeseCake.melt(), True)

    def testFruistWaffle(self):
        self.assertEqual(self.fruitsWaffle.getName(), 'FruitsWaffle')
        self.assertEqual(self.fruitsWaffle.getPrice(), 6000)
        self.assertEqual(self.fruitsWaffle.isIced(), True)
        self.assertEqual(self.fruitsWaffle.isMelted(), False)
        self.assertEqual(self.fruitsWaffle.melt(), True)
        self.assertEqual(self.fruitsWaffle.getMango(), 1)
        self.assertEqual(self.fruitsWaffle.getStrawberry(), 1)
        self.assertEqual(self.fruitsWaffle.getBlueberry(), 1)
        amount = randint(1, 5)
        CompareWaffle = self.fruitsWaffle.getnumWaffles()
        CompareMango = self.fruitsWaffle.getMango()
        CompareStrawberry = self.fruitsWaffle.getStrawberry()
        CompareBlueberry = self.fruitsWaffle.getBlueberry()

        ComparePrice = self.fruitsWaffle.getPrice()
        self.fruitsWaffle.addWaffle(amount)
        self.assertEqual(self.fruitsWaffle.getnumWaffles(),
                         CompareWaffle + amount)
        self.assertEqual(self.fruitsWaffle.getPrice(),
                         ComparePrice + amount * 1000)

        ComparePrice = self.fruitsWaffle.getPrice()
        self.fruitsWaffle.addFruitsMango(amount)
        self.assertEqual(self.fruitsWaffle.getMango(), CompareMango + amount)
        self.assertEqual(self.fruitsWaffle.getPrice(),
                         ComparePrice + amount * 1000)

        ComparePrice = self.fruitsWaffle.getPrice()
        self.fruitsWaffle.addFruitsStrawberry(amount)
        self.assertEqual(self.fruitsWaffle.getStrawberry(),
                         CompareStrawberry + amount)
        self.assertEqual(self.fruitsWaffle.getPrice(),
                         ComparePrice + amount * 1000)

        ComparePrice = self.fruitsWaffle.getPrice()
        self.fruitsWaffle.addFruitsBlueberry(amount)
        self.assertEqual(self.fruitsWaffle.getBlueberry(),
                         CompareBlueberry + amount)
        self.assertEqual(self.fruitsWaffle.getPrice(),
                         ComparePrice + amount * 1000)

    def testIceWaffle(self):
        self.assertEqual(self.iceWaffle.getName(), 'IceWaffle')
        self.assertEqual(self.iceWaffle.getPrice(), 6000)
        self.assertEqual(self.iceWaffle.isMelted(), False)
        self.assertEqual(self.iceWaffle.melt(), True)
        self.assertEqual(self.iceWaffle.geticeCream(), 2)
        amount = randint(1, 5)
        CompareWaffle = self.iceWaffle.getnumWaffles()
        CompareiceCream = self.iceWaffle.geticeCream()

        ComparePrice = self.iceWaffle.getPrice()
        self.iceWaffle.addWaffle(amount)
        self.assertEqual(self.iceWaffle.getnumWaffles(),
                         CompareWaffle + amount)
        self.assertEqual(self.iceWaffle.getPrice(),
                         ComparePrice + amount * 1000)

        ComparePrice = self.iceWaffle.getPrice()
        self.iceWaffle.addIceCream(amount)
        self.assertEqual(self.iceWaffle.geticeCream(),
                         CompareiceCream + amount)
        self.assertEqual(self.iceWaffle.getPrice(),
                         ComparePrice + amount * 500)

    def testRainbowCheeseCake(self):
        self.assertEqual(self.rainbowCheeseCake.getName(), 'RainbowCheeseCake')
        self.assertEqual(self.rainbowCheeseCake.getPrice(), 5500)
        self.assertEqual(self.rainbowCheeseCake.isIced(), True)
        self.assertEqual(self.rainbowCheeseCake.getMascapone(), 2)
        self.assertEqual(self.rainbowCheeseCake.isMelted(), False)
        self.assertEqual(self.rainbowCheeseCake.melt(), True)

    def testRedVelvetCheeseCake(self):
        self.assertEqual(self.redVelvetCheeseCake.getName(),
                         'RedVelvetCheeseCake')
        self.assertEqual(self.redVelvetCheeseCake.getPrice(), 6000)
        self.assertEqual(self.redVelvetCheeseCake.isIced(), True)
        self.assertEqual(self.redVelvetCheeseCake.getMascapone(), 2)
        self.assertEqual(self.redVelvetCheeseCake.getredVelvetPowder(), 2)
        self.assertEqual(self.redVelvetCheeseCake.isMelted(), False)
        self.assertEqual(self.redVelvetCheeseCake.melt(), True)
        ComparePowder = self.redVelvetCheeseCake.getredVelvetPowder()
        ComparePrice = self.redVelvetCheeseCake.getPrice()
        amount = randint(1, 5)
        self.redVelvetCheeseCake.addRedVelvetPowder(amount)
        self.assertEqual(self.redVelvetCheeseCake.getredVelvetPowder(),
                         ComparePowder + amount)
        self.assertEqual(self.redVelvetCheeseCake.getPrice(),
                         ComparePrice + (amount * 500))

    def testTiramisuCake(self):
        self.assertEqual(self.tiramisuCake.getName(), 'TiramisuCake')
        self.assertEqual(self.tiramisuCake.getPrice(), 5500)
        self.assertEqual(self.tiramisuCake.isIced(), True)
        self.assertEqual(self.tiramisuCake.getMascapone(), 2)
        self.assertEqual(self.tiramisuCake.getChocolatePowder(), 1)
        self.assertEqual(self.tiramisuCake.isMelted(), False)
        self.assertEqual(self.tiramisuCake.melt(), True)
        amount = randint(1, 5)
        ComparePowder = self.tiramisuCake.getChocolatePowder()
        self.tiramisuCake.addChocolatePowder(amount)
        self.assertEqual(self.tiramisuCake.getChocolatePowder(),
                         ComparePowder + amount)
