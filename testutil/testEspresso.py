from com.kakao.cafe.menu.espresso.espresso import Espresso
from com.kakao.cafe.menu.espresso.americano import Americano
from com.kakao.cafe.menu.espresso.cafeMocha import CafeMocha
from com.kakao.cafe.menu.espresso.caramelMacchiato import CaramelMacchiato
from com.kakao.cafe.menu.espresso.cappuccino import Cappuccino
from com.kakao.cafe.menu.espresso.latte import Latte
from com.kakao.cafe.menu.espresso.vanillaLatte import VanillaLatte
from com.kakao.cafe.menu.espresso.greenTeaLatte import GreenTeaLatte
from random import randint, uniform

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
        pastPrice, pastShot, amount = self.espresso.getPrice(
        ), self.espresso.getShot(), uniform(1.0, 5.0)
        self.espresso.addShot(amount)
        self.assertEqual(self.espresso.getPrice(), pastPrice + amount * 500)
        self.assertEqual(self.espresso.getShot(), pastShot + amount)

    def testAmericano(self):
        self.assertEqual(self.americano.getName(), "Americano")
        self.assertEqual(self.americano.getPrice(), 3000)
        self.assertEqual(self.americano.getWater(), 350)
        pastPrice, pastShot, amount = self.americano.getPrice(
        ), self.americano.getShot(), uniform(1.0, 5.0)
        self.americano.addShot(amount)
        self.assertEqual(self.americano.getPrice(), pastPrice + amount * 500)
        self.assertEqual(self.americano.getShot(), pastShot + amount)

    def testCafeMocha(self):
        self.assertEqual(self.cafemocha.getName(), "CafeMocha")
        self.assertEqual(self.cafemocha.getPrice(), 4000)
        pastMocha, pastPrice, amount = self.cafemocha.getMocha(
        ), self.cafemocha.getPrice(), randint(1, 5)
        self.cafemocha.addMocha(amount)
        self.assertEqual(self.cafemocha.getPrice(), pastPrice + amount * 300)
        self.assertEqual(self.cafemocha.getMocha(), pastMocha + amount)

    def testCaramelMacchiato(self):
        self.assertEqual(self.caramelmacchiato.getName(), "CaramelMacchiato")
        self.assertEqual(self.caramelmacchiato.getPrice(), 4000)
        pastCaramelSyrup, pastPrice, amount = self.caramelmacchiato.getCaramelSyrup(
        ), self.caramelmacchiato.getPrice(), randint(1, 5)
        self.caramelmacchiato.addCaramelSyrup(amount)
        self.assertEqual(self.caramelmacchiato.getPrice(),
                         pastPrice + amount * 200)
        self.assertEqual(self.caramelmacchiato.getCaramelSyrup(),
                         pastCaramelSyrup + amount)

    def testCappuccino(self):
        self.assertEqual(self.cappuccino.getName(), "Cappuccino")
        self.assertEqual(self.cappuccino.getPrice(), 4500)
        self.assertEqual(self.cappuccino.getMilk(), 250)
        pastCinnamon, amount = self.cappuccino.getCinnamon(), randint(1, 5)
        self.cappuccino.addCinnamon(amount)
        self.assertEqual(self.cappuccino.getCinnamon(), pastCinnamon + amount)

    def testLatte(self):
        self.assertEqual(self.latte.getName(), "Latte")
        self.assertEqual(self.latte.getPrice(), 4000)
        self.assertEqual(self.latte.getMilk(), 300)
        self.assertEqual(self.latte.getWater(), 350)
        pastPrice, pastShot, amount = self.latte.getPrice(
        ), self.latte.getShot(), uniform(1.0, 5.0)
        self.latte.addShot(amount)
        self.assertEqual(self.latte.getPrice(), pastPrice + amount * 500)
        self.assertEqual(self.latte.getShot(), pastShot + amount)

    def testVanillaLatte(self):
        self.assertEqual(self.vanillaLatte.getName(), "VanillaLatte")
        self.assertEqual(self.vanillaLatte.getPrice(), 4000)
        pastVanillaSyrup, pastPrice, amount = self.vanillaLatte.getVanillaSyrup(
        ), self.vanillaLatte.getPrice(), randint(1, 5)
        self.vanillaLatte.addVanillaSyrup(amount)
        self.assertEqual(self.vanillaLatte.getVanillaSyrup(),
                         pastVanillaSyrup + amount)
        self.assertEqual(self.vanillaLatte.getPrice(),
                         pastPrice + amount * 200)

    def testGreenTeaLatete(self):
        self.assertEqual(self.greenTeaLatte.getName(), "GreenTeaLatte")
        self.assertEqual(self.greenTeaLatte.getPrice(), 4000)
        pastCondensedMilk, pastGreenTea, pastPrice, amount = self.greenTeaLatte.getCondensedMilk(
        ), self.greenTeaLatte.getGreenTea(), self.greenTeaLatte.getPrice(
        ), randint(1, 5)
        self.greenTeaLatte.addCondensedMilk(amount)
        self.greenTeaLatte.addGreenTea(amount)
        self.assertEqual(self.greenTeaLatte.getCondensedMilk(),
                         pastCondensedMilk + amount)
        self.assertEqual(self.greenTeaLatte.getPrice(),
                         pastPrice + amount * 300)
        self.assertEqual(self.greenTeaLatte.getGreenTea(),
                         pastGreenTea + amount)


if __name__ == "__main__":
    unittest.main()