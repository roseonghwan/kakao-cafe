from com.kakao.cafe.module.menuPrinter import MenuPrinter
import unittest


class TestMenuPrinter(unittest.TestCase):
    def setUp(self):
        self.menuList = MenuPrinter()

    def testGetMenuList(self):
        self.assertEqual(self.menuList.getMenulist(), "")

    def testPrint(self):
        self.assertEqual(self.menuList.Print(), "")


if __name__ == "__main__":
    unittest.main()