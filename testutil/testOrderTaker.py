from com.kakao.cafe.module.menuPrinter import MenuPrinter
from com.kakao.cafe.module.orderTaker import OrderTaker
from com.kakao.cafe.cafe import *

import unittest
from random import randint, choice


class TestOrderTaker(unittest.TestCase):
    def setUp(self):
        self.menuList = MenuPrinter()
        self.addList = OrderTaker()
        '''
        self.testList = list()
        for i in range(randint(1, 3)):
            self.testList.append(choice(self.menuList.getMenulist()))
            self.testList.append(randint(1, 50))
            self.testList.append(choice(self.addList.getAddlist()))
        '''

        self.assertEquals(self.testList, self.addList.getOrderlist())


if __name__ == "__main__":
    unittest.main()