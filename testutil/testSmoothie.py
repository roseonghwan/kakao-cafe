from com.kakao.cafe.menu.smoothie.smoothie import Smoothie
from com.kakao.cafe.menu.smoothie.berryBerrySmoothie import BerryBerrySmoothie
from com.kakao.cafe.menu.smoothie.pineappleSmoothie import PineappleSmoothie
from com.kakao.cafe.menu.smoothie.yogurtSmoothie import YogurtSmoothie

import unittest


class TestSmoothie(unittest.TestCase):
    def setUp(self):
        self.berryBerrySmoothie = BerryBerrySmoothie()
        self.berryBerrySmoothie.addBerry(5)

        self.pineappleSmoothie = PineappleSmoothie()
        self.pineappleSmoothie.addPineapple(5)

        self.yogurtSmoothie = YogurtSmoothie()
        self.yogurtSmoothie.addYogurt(5)

        try:
            self.abstract = Smoothie()

        except TypeError as TE:
            self.abstract = TE.__str__()

    def testInstantiation(self):
        self.assertEqual(
            self.abstract,
            "Can't instantiate abstract class Smoothie with abstract methods getGroundIce, getName, getPrice, isIced, setGroundIce, setIced, setName, setPrice"
        )

    def testBerryBerrySmoothie(self):
        self.assertEqual(self.berryBerrySmoothie.getName(),
                         "BerryBerrySmoothie")
        self.assertEqual(self.berryBerrySmoothie.getPrice(), 7500)
        self.assertEqual(self.berryBerrySmoothie.getGroundIce(), 400)
        self.assertEqual(self.berryBerrySmoothie.getMixedBerry(), 6)

    def testPineappleSmoothie(self):

        self.assertEqual(self.pineappleSmoothie.getName(), "PineappleSmoothie")
        self.assertEqual(self.pineappleSmoothie.getPrice(), 7500)
        self.assertEqual(self.pineappleSmoothie.getGroundIce(), 400)
        self.assertEqual(self.pineappleSmoothie.getPineApple(), 6)

    def testYogurtSmoothie(self):

        self.assertEqual(self.yogurtSmoothie.getName(), "YogurtSmoothie")
        self.assertEqual(self.yogurtSmoothie.getPrice(), 7500)
        self.assertEqual(self.yogurtSmoothie.getGroundIce(), 400)
        self.assertEqual(self.yogurtSmoothie.getYogurt(), 6)

    def testSmoothie(self):
        self.assertEqual(0, 0)


if __name__ == "__main__":
    unittest.main()
