from com.kakao.cafe.menu.cafeMenu import CafeMenu

import unittest


class TestCafeMenu(unittest.TestCase):
    def setUp(self):
        try:
            self.impossible = CafeMenu()

        except TypeError as TE:
            self.impossible = TE.__str__()

    def testInstantiation(self):
        self.assertEqual(
            self.impossible,
            "Can't instantiate abstract class CafeMenu with abstract methods getName, getPrice, isIced, setIced, setName, setPrice"
        )


if __name__ == '__main__':
    unittest.main()
