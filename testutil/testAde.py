from com.kakao.cafe.menu.ade.ade import Ade
from com.kakao.cafe.menu.ade.lemonAde import LemonAde
from com.kakao.cafe.menu.ade.orangeAde import OrangeAde
from com.kakao.cafe.menu.ade.strawberryAde import StrawberryAde
from random import randint, uniform

import unittest


class TestAde(unittest.TestCase):
    def setUp(self):
        self.LemonAde = LemonAde()
        self.OrangeAde = OrangeAde()
        self.StrawberryAde = StrawberryAde()

    def testLemonAde(self):
        self.assertEqual(self.LemonAde.getName(), 'LemonAde')
        self.assertEqual(self.LemonAde.getPrice(), 3500)
        self.assertEqual(self.LemonAde.isIced(), True)
        pastPrice, pastLemon, amount = self.LemonAde.getPrice(
        ), self.LemonAde.getLemon(), uniform(1.0, 5.0)
        self.LemonAde.addLemon(amount)
        self.assertEqual(self.LemonAde.getPrice(), pastPrice + amount * 500)
        self.assertEqual(self.LemonAde.getLemon(), pastLemon + amount)

    def testOrangeAde(self):
        self.assertEqual(self.OrangeAde.getName(), 'OrangeAde')
        self.assertEqual(self.OrangeAde.getPrice(), 3500)
        self.assertEqual(self.OrangeAde.isIced(), True)
        pastPrice, pastOrange, amount = self.OrangeAde.getPrice(
        ), self.OrangeAde.getOrange(), uniform(1.0, 5.0)
        self.OrangeAde.addOrange(amount)
        self.assertEqual(self.OrangeAde.getPrice(), pastPrice + amount * 500)
        self.assertEqual(self.OrangeAde.getOrange(), pastOrange + amount)

    def testStrawberryAde(self):
        self.assertEqual(self.StrawberryAde.getName(), 'StrawberryAde')
        self.assertEqual(self.StrawberryAde.getPrice(), 3500)
        self.assertEqual(self.StrawberryAde.isIced(), True)
        pastPrice, pastStrawberry, amount = self.StrawberryAde.getPrice(
        ), self.StrawberryAde.getStrawberry(), uniform(1.0, 5.0)
        self.StrawberryAde.addStrawberry(amount)
        self.assertEqual(self.StrawberryAde.getPrice(),
                         pastPrice + amount * 500)
        self.assertEqual(self.StrawberryAde.getStrawberry(),
                         pastStrawberry + amount)


if __name__ == '__main__':
    unittest.main()
