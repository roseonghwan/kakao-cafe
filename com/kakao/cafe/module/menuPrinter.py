from com.kakao.cafe.module.cafeWorker import CafeWorker
from com.kakao.cafe.menu.espresso.espresso import Espresso
from com.kakao.cafe.menu.espresso.americano import Americano
from com.kakao.cafe.menu.espresso.latte import Latte
from com.kakao.cafe.menu.espresso.greenTeaLatte import GreenTeaLatte
from com.kakao.cafe.menu.espresso.vanillaLatte import VanillaLatte
from com.kakao.cafe.menu.espresso.cafeMocha import CafeMocha
from com.kakao.cafe.menu.espresso.cappuccino import Cappuccino
from com.kakao.cafe.menu.espresso.caramelMacchiato import CaramelMacchiato
from com.kakao.cafe.menu.ade.lemonAde import LemonAde
from com.kakao.cafe.menu.ade.orangeAde import OrangeAde
from com.kakao.cafe.menu.smoothie.yogurtSmoothie import YogurtSmoothie
from com.kakao.cafe.menu.smoothie.berryBerrySmoothie import BerryBerrySmoothie
from com.kakao.cafe.menu.smoothie.pineappleSmoothie import PineappleSmoothie
from com.kakao.cafe.menu.ade.strawberryAde import StrawberryAde
from com.kakao.cafe.menu.tea.chamomileTea import ChamomileTea
from com.kakao.cafe.menu.tea.greenTea import GreenTea
from com.kakao.cafe.menu.tea.hibiscusTea import HibiscusTea
from com.kakao.cafe.menu.tea.iceTea import IceTea
from com.kakao.cafe.menu.tea.lavenderTea import LavenderTea
from com.kakao.cafe.menu.tea.milkTea import MilkTea
from com.kakao.cafe.menu.tea.royalMilkTea import RoyalMilkTea
from com.kakao.cafe.menu.tea.matchaMilkTea import MatchaMilkTea
from com.kakao.cafe.menu.tea.peppermintTea import PeppermintTea
from com.kakao.cafe.menu.tea.rooibosTea import RooibosTea


class MenuPrinter(CafeWorker):
    def __init__(self):
        self.__menuList = dict()
        self.__menuList['Coffee'] = list()
        self.__menuList['Ade'] = list()
        self.__menuList['Smoothie'] = list()
        self.__menuList['Tea'] = list()
        self.__menuList['Coffee'].append(Espresso())
        self.__menuList['Coffee'].append(Americano())
        self.__menuList['Coffee'].append(Latte())
        self.__menuList['Coffee'].append(GreenTeaLatte())
        self.__menuList['Coffee'].append(VanillaLatte())
        self.__menuList['Coffee'].append(CafeMocha())
        self.__menuList['Coffee'].append(Cappuccino())
        self.__menuList['Coffee'].append(CaramelMacchiato())
        self.__menuList['Ade'].append(LemonAde())
        self.__menuList['Ade'].append(OrangeAde())
        self.__menuList['Ade'].append(StrawberryAde())
        self.__menuList['Smoothie'].append(YogurtSmoothie())
        self.__menuList['Smoothie'].append(BerryBerrySmoothie())
        self.__menuList['Smoothie'].append(PineappleSmoothie())
        self.__menuList['Tea'].append(ChamomileTea())
        self.__menuList['Tea'].append(GreenTea())
        self.__menuList['Tea'].append(HibiscusTea())
        self.__menuList['Tea'].append(IceTea())
        self.__menuList['Tea'].append(LavenderTea())
        self.__menuList['Tea'].append(MilkTea())
        self.__menuList['Tea'].append(RoyalMilkTea())
        self.__menuList['Tea'].append(MatchaMilkTea())
        self.__menuList['Tea'].append(PeppermintTea())
        self.__menuList['Tea'].append(RooibosTea())

    def getMenulist(self) -> dict:
        return self.__menuList

    def Print(self):
        print("Kakao Cafe")
        print("----------------------------------------")
        for i in self.__menuList:
            print("%-10s" % i, end="")
        print()
        print("----------------------------------------")
        s = list()
        for i in self.__menuList:
            for j in self.__menuList[i]:
                s[j] += "%-10s" % self.__menuList[i][j].getName()
                s[j] += "%10s" % self.__menuList[i][j].getPrice()

        for i in range(len(s)):
            print(s[i])


if __name__ == "__main__":
    m = MenuPrinter()
    m.Print()
