from com.kakao.cafe.menu.smoothie.smoothie import Smoothie
from com.kakao.cafe.menu.smoothie.berryBerrySmoothie import BerryBerrySmoothie
import unittest


class TestSmoothie(unittest.TestCase):
    def setUp(self):
        self.berryBerrySmoothie = BerryBerrySmoothie()
        self.berryBerrySmoothie.addBerry(3)
        try:
            self.impossible = Smoothie()

        except TypeError as TE:
            self.impossible = TE.__str__()

    def testInstantiation(self):
        self.assertEqual(
            self.impossible,
            "Can't instantiate abstract class Smoothie with abstract methods getGroundIce, getName, getPrice, isIced, setGroundIce, setIced, setName, setPrice"
        )

    def testBerryBerrySmoothie(self):
        self.assertEqual(self.berryBerrySmoothie.getName(),
                         'BerryBerrySmoothie')
        self.assertEqual(self.berryBerrySmoothie.getPrice(), 6500)
        self.assertEqual(self.berryBerrySmoothie.isIced(), True)


if __name__ == '__main__':
    unittest.main()
