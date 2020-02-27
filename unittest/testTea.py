from com.kakao.cafe.menu.tea_menu.tea import Tea
from com.kakao.cafe.menu.tea_menu.icetea import IceTea
from com.kakao.cafe.menu.tea_menu.chamomiletea import ChamomileTea
from com.kakao.cafe.menu.tea_menu.greentea import GreenTea
from com.kakao.cafe.menu.tea_menu.lavendertea import LavenderTea
from com.kakao.cafe.menu.tea_menu.hibiscustea import HibiscusTea
from com.kakao.cafe.menu.tea_menu.pepperminttea import PeppermintTea
from com.kakao.cafe.menu.tea_menu.rooibostea import RooibosTea
from com.kakao.cafe.menu.tea_menu.milktea import MilkTea
from com.kakao.cafe.menu.tea_menu.royalmilktea import RoyalMilkTea
from com.kakao.cafe.menu.tea_menu.matchamilktea import MatchaMilkTea

import unittest
import random


class TestTea(unittest.TestCase):
    def setUp(self):
        self.tea = Tea()
        self.icetea = IceTea()
        self.chamomiletea = ChamomileTea()
        self.greentea = GreenTea()
        self.lavnedertea = LavenderTea()
        self.hibiscustea = HibiscusTea()
        self.pepperminttea = PeppermintTea()
        self.rooibostea = RooibosTea()
        self.milktea = MilkTea()
        self.royalmilktea = RoyalMilkTea()
        self.matchamilktea = MatchaMilkTea()

    def testIceTea(self):
        self.assertEqual(self.icetea.getName(), 'IceTea')
        self.assertEqual(self.icetea.getPrice(), 3000)
        self.assertEqual(self.icetea.getWater(), 300)
        self.assertEqual(self.icetea.isIced(), True)
        self.assertEqual(self.icetea.getpeachPowder(), 1)
        originPeachPowder = self.icetea.getpeachPowder()
        originPrice = self.icetea.getPrice()
        amount = 2
        self.assertEqual(self.icetea.getpeachPowder(),
                         originPeachPowder + amount)
        self.assertEqual(self.icetea.getPrice(), originPrice + amount * 400)

    def testChamomileTea(self):
        self.assertEqual(self.chamomiletea.getName(), 'ChamomileTea')
        self.assertEqual(self.chamomiletea.getPrice(), 3500)
        self.assertEqual(self.chamomiletea.getWater(), 400)
        self.assertEqual(self.chamomiletea.getchamomileTea + (), 1)
        originPrice = self.chamomiletea.getPrice()
        originChamomileTea = self.chamomiletea.getchamomileTea()
        amount = 2
        self.assertEqual(self.chamomiletea.getchamomileTea() +
                         originChamomileTea + amount)
        self.assertEqual(self.chamomiletea.getPrice() + originPrice +
                         amount * 500)

    def testGreenTea(self):
        self.assertEqual(self.greentea.getName(), 'GreenTea')
        self.assertEqual(self.greentea.getPrice(), 3000)
        self.assertEqual(self.greentea.getWater(), 200)
        self.assertEqual(self.greentea.getgreenTea(), 1)
        originGreenTea = self.greentea.getgreenTea()
        originPrice = self.greentea.getPrice()
        amount = 2
        self.assertEqual(self.greentea.getgreenTea(), originGreenTea + amount)
        self.assertEqual(self.greentea.getPrice(), originPrice + amount * 500)

    def testLavenderTea(self):
        self.assertEqual(self.lavnedertea.getName(), 'LavenderTea')
        self.assertEqual(self.lavnedertea.getPrice(), 3500)
        self.assertEqual(self.lavnedertea.getWater(), 300)
        self.assertEqual(self.lavnedertea.getlavenderTea(), 1)
        originLavenderTea = self.lavnedertea.getlavenderTea()
        originPrice = self.lavnedertea.getPrice()
        amount = 2
        self.assertEqual(self.lavnedertea.getlavenderTea(),
                         originLavenderTea + amount)
        self.assertEqual(self.lavnedertea.getPrice(),
                         originPrice + amount * 500)

    def testHibiscusTea(self):
        self.assertEqual(self.hibiscustea.getName(), 'HibiscusTea')
        self.assertEqual(self.hibiscustea.getPrice(), 3000)
        self.assertEqual(self.hibiscustea.getWater(), 200)
        self.assertEqual(self.hibiscustea.gethibiscusTea(), 1)
        originHibiscusTea = self.hibiscustea.gethibiscusTea()
        originPrice = self.hibiscustea.getPrice()
        amount = 2
        self.assertEqual(self.hibiscustea.gethibiscusTea(),
                         originHibiscusTea + amount)
        self.assertEqual(self.hibiscustea.getPrice(),
                         originPrice + amount * 500)

    def testPeppermintTea(self):
        self.assertEqual(self.pepperminttea.getName(), 'PeppermintTea')
        self.assertEqual(self.pepperminttea.getPrice(), 3500)
        self.assertEqual(self.pepperminttea.getWater(), 350)
        self.assertEqual(self.pepperminttea.getpeppermintTea(), 1)
        originPepperMintTea = self.pepperminttea.getpeppermintTea()
        originPrice = self.pepperminttea.getPrice()
        amount = 2
        self.assertEqual(self.pepperminttea.getpeppermintTea(),
                         originPepperMintTea + amount)
        self.assertEqual(self.pepperminttea.getPrice(),
                         originPrice + amount * 500)

    def testRoobibosTea(self):
        self.assertEqual(self.rooibostea.getName(), 'RoobibosTea')
        self.assertEqual(self.rooibostea.getPrice(), 4000)
        self.assertEqual(self.rooibostea.getWater(), 300)
        self.assertEqual(self.rooibostea.getroobibosTea(), 1)
        originRoobibosTea = self.rooibostea.getroobibosTea()
        originPrice = self.rooibostea.getPrice()
        amount = 2
        self.assertEqual(self.rooibostea.getroobibosTea(),
                         originRoobibosTea + amount)
        self.assertEqual(self.rooibostea.getPrice(),
                         originPrice + amount * 700)

    def testRoyalMilkTea(self):
        self.assertEqual(self.royalmilktea.getName(), 'RoyalMilkTea')
        self.assertEqual(self.royalmilktea.getPrice(), 5000)
        self.assertEqual(self.royalmilktea.getMilk(), 350)
        self.assertEqual(self.royalmilktea.getblackTea(), 2)
        self.assertEqual(self.royalmilktea.getroyalHoney(), 1)
        originBlackTea = self.royalmilktea.getBlackTea()
        originRoyalHoney = self.royalmilktea.getroyalHoney()
        originPrice = self.royalmilktea.getPrice()
        addedBlacktea = 1
        subtractedBlacktea = 1
        addedRoyalHoney = 1

        self.assertEqual(self.royalmilktea.getBlackTea(),
                         originBlackTea + -subtractedBlacktea)
        self.assertEqual(self.royalmilktea.getroyalHoney(),
                         originRoyalHoney + addedRoyalHoney)
        self.assertEqual(
            self.royalmilktea.getPrice(),
            originPrice + addedBlacktea * 500 + addedRoyalHoney * 1000)

    def testMatchaMilkTea(self):
        self.assertEqual(self.matchamilktea.getName(), 'MatchaMilkTea')
        self.assertEqual(self.matchamilktea.getPrice(), 4500)
        self.assertEqual(self.matchamilktea.getMilk(), 400)
        self.assertEqual(self.matchamilktea.getBlackTea(), 2)
        self.assertEqual(self.matchamilktea.getCondensedMilk(), 1)
        self.assertEqual(self.matchamilktea.getMatcha(), 1)
        originBlackTea = self.matchamilktea.getBlackTea()
        originCondensedMilk = self.matchamilktea.getCondensedMilk()
        originMatcha = self.matchamilktea.getMatcha()
        originPrice = self.matchamilktea.getPrice()
        addedBlacktea = 0
        subtractedBlacktea = 1
        addedCondensedMilk = 1
        addedMatch = 2
        self.assertEqual(self.matchamilktea.getBlackTea(),
                         originBlackTea + addedBlacktea - subtractedBlacktea)
        self.assertEqual(
            self.matchamilktea.getPrice(), originPrice + addedBlacktea * 500 +
            addedCondensedMilk * 500 + addedMatch * 400)


if __name__ == "__main__":
    unittest.main()