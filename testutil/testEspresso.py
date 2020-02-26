from com.kakao.cafe.menu.espresso.espresso import Espresso
from com.kakao.cafe.menu.espresso.americano import Americano
from com.kakao.cafe.menu.espresso.cafeMocha import CafeMocha
from com.kakao.cafe.menu.espresso.caramelMacchiato import CaramelMacchiato
from com.kakao.cafe.menu.espresso.cappuccino import Cappuccino
from com.kakao.cafe.menu.espresso.latte import Latte
from com.kakao.cafe.menu.espresso.vanillaLatte import VanillaLatte
from com.kakao.cafe.menu.espresso.greenTeaLatte import GreenTeaLatte
from random import randint

import unittest


class TestEspresso(unittest.TestCase):
    def setUp(self):
        self.espresso = Espresso()
        self.americano = Americano()
        self.cafemocha = CafeMocha()
        self.caramelmacchiato = CaramelMacchiato()
        self.cappuccino = Cappuccino()
        self.latte = Latte()
        self.vanillaLatte = VanillaLatte()
        self.greenTeaLatte = GreenTeaLatte()

    def testEspresso(self):
        self.assertEqual(self.espresso.getName(), "Espresso")
        self.assertEqual(self.espresso.getPrice(), 2500)
        self.assertEqual(self.espresso.isIced(), False)
        # 샷 추가 가격 비교
        pastPrice, pastShot, sh = self.espresso.getPrice(
        ), self.espresso.getShot(), randint(1, 5)
        self.espresso.addShot(sh)
        self.assertEqual(self.espresso.getPrice(), pastPrice + sh * 500)

    def testAmericano(self):
        self.assertEqual(self.americano.getName(), "Americano")
        self.assertEqual(self.americano.getPrice(), 3000)
        self.assertEqual(self.americano.getWater(), 350)
        # 샷 추가 가격 비교

    def testCafeMocha(self):
        self.assertEqual(self.cafemocha.getName(), "CafeMocha")
        self.assertEqual(self.cafemocha.getPrice(), 4000)
        # 모카 추가 가격 비교

    def testCaramelMacchiato(self):
        self.assertEqual(self.caramelmacchiato.getName(), "CaramelMacchiato")
        self.assertEqual(self.caramelmacchiato.getPrice(), 4000)
        # 카라멜 추가 가격 비교

    def testCappuccino(self):
        self.assertEqual(self.cappuccino.getName(), "Cappuccino")
        self.assertEqual(self.cappuccino.getPrice(), 4500)
        # 시나몬 추가 가격 비교

    def testLatte(self):
        self.assertEqual(self.latte.getName(), "Latte")
        self.assertEqual(self.latte.getPrice(), 4000)
        self.assertEqual(self.latte.getMilk(), 300)
        self.assertEqual(self.latte.getWater(), 350)
        self.assertEqual(self.latte.getShot(), 2.0)

    def testVanillaLatte(self):
        self.assertEqual(self.vanillaLatte.getName(), "VanillaLatte")
        self.assertEqual(self.vanillaLatte.getPrice(), 4000)
        # 바나나 시럽 테스트

    def testGreenTeaLatete(self):
        self.assertEqual(self.greenTeaLatte.getName(), "GreenTeaLatte")
        self.assertEqual(self.greenTeaLatte.getPrice(), 4000)
        # 연유, 녹차 추가 테스트


if __name__ == "__main__":
    unittest.main()