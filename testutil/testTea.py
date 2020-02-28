from com.kakao.cafe.menu.tea.tea import Tea
from com.kakao.cafe.menu.tea.iceTea import IceTea
from com.kakao.cafe.menu.tea.chamomileTea import ChamomileTea
from com.kakao.cafe.menu.tea.greenTea import GreenTea
from com.kakao.cafe.menu.tea.lavenderTea import LavenderTea
from com.kakao.cafe.menu.tea.hibiscusTea import HibiscusTea
from com.kakao.cafe.menu.tea.peppermintTea import PeppermintTea
from com.kakao.cafe.menu.tea.rooibosTea import RooibosTea
from com.kakao.cafe.menu.tea.milkTea import MilkTea
from com.kakao.cafe.menu.tea.royalMilkTea import RoyalMilkTea
from com.kakao.cafe.menu.tea.matchaMilkTea import MatchaMilkTea

import unittest


class TestTea(unittest.TestCase):
    def setUp(self):
        self.icetea = IceTea()
        self.chamomiletea = ChamomileTea()
        self.greentea = GreenTea()
        self.lavnedertea = LavenderTea()
        self.hibiscustea = HibiscusTea()
        self.pepperminttea = PeppermintTea()
        self.rooibostea = RooibosTea()
        self.royalmilktea = RoyalMilkTea()
        self.matchamilktea = MatchaMilkTea()

        try:
            self.impossible1 = Tea()
        except TypeError as TE:
            self.impossible1 = TE.__str__()

        try:
            self.impossible2 = MilkTea()
        except TypeError as TE:
            self.impossible2 = TE.__str__()

    def testTea(self):
        self.assertEqual(
            self.impossible1,
            "Can't instantiate abstract class Tea with abstract methods getName, getPrice, getWater, isIced, setIced, setName, setPrice, setWater"
        )

    def testIceTea(self):
        self.assertEqual(self.icetea.getName(), 'IceTea')
        self.assertEqual(self.icetea.getPrice(), 3000)
        self.assertEqual(self.icetea.getWater(), 300)
        self.assertEqual(self.icetea.isIced(), True)
        self.assertEqual(self.icetea.getPeachPowder(), 1)
        originPeachPowder = self.icetea.getPeachPowder()
        originPrice = self.icetea.getPrice()
        amount = 2
        self.icetea.addPeachPowder(amount)
        self.assertEqual(self.icetea.getPeachPowder(),
                         originPeachPowder + amount)
        self.assertEqual(self.icetea.getPrice(), originPrice + amount * 400)

    def testChamomileTea(self):
        self.assertEqual(self.chamomiletea.getName(), 'ChamomileTea')
        self.assertEqual(self.chamomiletea.getPrice(), 3500)
        self.assertEqual(self.chamomiletea.getWater(), 400)
        self.assertEqual(self.chamomiletea.getChamomileTea(), 1)
        originPrice = self.chamomiletea.getPrice()
        originChamomileTea = self.chamomiletea.getChamomileTea()
        amount = 2
        self.chamomiletea.addChamomileTea(amount)
        self.assertEqual(self.chamomiletea.getChamomileTea(),
                         originChamomileTea + amount)
        self.assertEqual(self.chamomiletea.getPrice(),
                         originPrice + amount * 500)

    def testGreenTea(self):
        self.assertEqual(self.greentea.getName(), 'GreenTea')
        self.assertEqual(self.greentea.getPrice(), 3000)
        self.assertEqual(self.greentea.getWater(), 200)
        self.assertEqual(self.greentea.getGreenTea(), 1)
        originGreenTea = self.greentea.getGreenTea()
        originPrice = self.greentea.getPrice()
        amount = 2
        self.greentea.addGreenTea(amount)
        self.assertEqual(self.greentea.getGreenTea(), originGreenTea + amount)
        self.assertEqual(self.greentea.getPrice(), originPrice + amount * 500)

    def testLavenderTea(self):
        self.assertEqual(self.lavnedertea.getName(), 'LavenderTea')
        self.assertEqual(self.lavnedertea.getPrice(), 3500)
        self.assertEqual(self.lavnedertea.getWater(), 300)
        self.assertEqual(self.lavnedertea.getLavenderTea(), 1)
        originLavenderTea = self.lavnedertea.getLavenderTea()
        originPrice = self.lavnedertea.getPrice()
        amount = 2
        self.lavnedertea.addLavenderTea(amount)
        self.assertEqual(self.lavnedertea.getLavenderTea(),
                         originLavenderTea + amount)
        self.assertEqual(self.lavnedertea.getPrice(),
                         originPrice + amount * 500)

    def testHibiscusTea(self):
        self.assertEqual(self.hibiscustea.getName(), 'HibiscusTea')
        self.assertEqual(self.hibiscustea.getPrice(), 3000)
        self.assertEqual(self.hibiscustea.getWater(), 200)
        self.assertEqual(self.hibiscustea.getHibiscusTea(), 1)
        originHibiscusTea = self.hibiscustea.getHibiscusTea()
        originPrice = self.hibiscustea.getPrice()
        amount = 2
        self.hibiscustea.addHibiscusTea(amount)
        self.assertEqual(self.hibiscustea.getHibiscusTea(),
                         originHibiscusTea + amount)
        self.assertEqual(self.hibiscustea.getPrice(),
                         originPrice + amount * 500)

    def testPeppermintTea(self):
        self.assertEqual(self.pepperminttea.getName(), 'PeppermintTea')
        self.assertEqual(self.pepperminttea.getPrice(), 3500)
        self.assertEqual(self.pepperminttea.getWater(), 350)
        self.assertEqual(self.pepperminttea.getPeppermintTea(), 1)
        originPepperMintTea = self.pepperminttea.getPeppermintTea()
        originPrice = self.pepperminttea.getPrice()
        amount = 2
        self.pepperminttea.addPeppermintTea(amount)
        self.assertEqual(self.pepperminttea.getPeppermintTea(),
                         originPepperMintTea + amount)
        self.assertEqual(self.pepperminttea.getPrice(),
                         originPrice + amount * 500)

    def testRooibosTea(self):
        self.assertEqual(self.rooibostea.getName(), 'RooibosTea')
        self.assertEqual(self.rooibostea.getPrice(), 4000)
        self.assertEqual(self.rooibostea.getWater(), 300)
        self.assertEqual(self.rooibostea.getRooibosTea(), 1)
        originRooibosTea = self.rooibostea.getRooibosTea()
        originPrice = self.rooibostea.getPrice()
        amount = 2
        self.rooibostea.addRooibosTea(amount)
        self.assertEqual(self.rooibostea.getRooibosTea(),
                         originRooibosTea + amount)
        self.assertEqual(self.rooibostea.getPrice(),
                         originPrice + amount * 700)

    def testMilkTea(self):
        self.assertEqual(
            self.impossible2,
            "Can't instantiate abstract class MilkTea with abstract methods getBlackTea, getMilk, getName, getPrice, getWater, isIced, setBlackTea, setIced, setMilk, setName, setPrice, setWater"
        )

    def testRoyalMilkTea(self):
        self.assertEqual(self.royalmilktea.getName(), 'RoyalMilkTea')
        self.assertEqual(self.royalmilktea.getPrice(), 5000)
        self.assertEqual(self.royalmilktea.getMilk(), 350)
        self.assertEqual(self.royalmilktea.getBlackTea(), 2)
        self.assertEqual(self.royalmilktea.getRoyalHoney(), 1)
        originBlackTea = self.royalmilktea.getBlackTea()
        originRoyalHoney = self.royalmilktea.getRoyalHoney()
        originPrice = self.royalmilktea.getPrice()
        addedBlacktea = 1
        subtractedBlacktea = 1
        addedRoyalHoney = 1
        self.royalmilktea.subBlackTea(subtractedBlacktea)
        self.royalmilktea.addBlackTea(addedBlacktea)
        self.royalmilktea.addRoyalHoney(addedRoyalHoney)
        self.assertEqual(self.royalmilktea.getBlackTea(),
                         originBlackTea + addedBlacktea - subtractedBlacktea)

        self.assertEqual(self.royalmilktea.getRoyalHoney(),
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
        addedBlacktea = 1
        subtractedBlacktea = 1
        addedCondensedMilk = 1
        addedMatch = 2
        self.matchamilktea.subBlackTea(subtractedBlacktea)
        self.matchamilktea.addBlackTea(addedBlacktea)
        self.matchamilktea.addCondensedMilk(addedCondensedMilk)
        self.matchamilktea.addMatcha(addedMatch)
        self.assertEqual(self.matchamilktea.getBlackTea(),
                         originBlackTea + addedBlacktea - subtractedBlacktea)
        self.assertEqual(self.matchamilktea.getCondensedMilk(),
                         originCondensedMilk + addedCondensedMilk)
        self.assertEqual(self.matchamilktea.getMatcha(),
                         originMatcha + addedMatch)
        self.assertEqual(
            self.matchamilktea.getPrice(), originPrice + addedBlacktea * 500 +
            addedCondensedMilk * 500 + addedMatch * 400)


if __name__ == "__main__":
    unittest.main()