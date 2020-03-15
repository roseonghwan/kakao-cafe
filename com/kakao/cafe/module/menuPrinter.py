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
from com.kakao.cafe.menu.dessert.belgianWaffle import BelgianWaffle
from com.kakao.cafe.menu.dessert.fruitsWaffle import FruitsWaffle
from com.kakao.cafe.menu.dessert.iceWaffle import IceWaffle
from com.kakao.cafe.menu.dessert.newYorkCheeseCake import NewYorkCheeseCake
from com.kakao.cafe.menu.dessert.rainbowCheeseCake import RainbowCheeseCake
from com.kakao.cafe.menu.dessert.redVelvetCheeseCake import RedVelvetCheeseCake
from com.kakao.cafe.menu.dessert.tiramisuCake import TiramisuCake


class MenuPrinter(CafeWorker):
    def __init__(self):
        self.__menuList = dict()
        self.__menuList['Espresso'] = list()
        self.__menuList['Ade'] = list()
        self.__menuList['Smoothie'] = list()
        self.__menuList['Tea'] = list()
        self.__menuList['Dessert'] = list()
        self.__menuList['Espresso'].append(Espresso())
        self.__menuList['Espresso'].append(Americano())
        self.__menuList['Espresso'].append(Latte())
        self.__menuList['Espresso'].append(GreenTeaLatte())
        self.__menuList['Espresso'].append(VanillaLatte())
        self.__menuList['Espresso'].append(CafeMocha())
        self.__menuList['Espresso'].append(Cappuccino())
        self.__menuList['Espresso'].append(CaramelMacchiato())
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
        self.__menuList['Tea'].append(RoyalMilkTea())
        self.__menuList['Tea'].append(MatchaMilkTea())
        self.__menuList['Tea'].append(PeppermintTea())
        self.__menuList['Tea'].append(RooibosTea())
        self.__menuList['Dessert'].append(BelgianWaffle())
        self.__menuList['Dessert'].append(FruitsWaffle())
        self.__menuList['Dessert'].append(IceWaffle())
        self.__menuList['Dessert'].append(NewYorkCheeseCake())
        self.__menuList['Dessert'].append(RainbowCheeseCake())
        self.__menuList['Dessert'].append(RedVelvetCheeseCake())
        self.__menuList['Dessert'].append(TiramisuCake())

    def getMenulist(self) -> dict:
        return self.__menuList

    def Print(self) -> None:
        print("Wellcome to Kakao Cafe!!")
        print(
            "------------------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        for i in self.__menuList:
            print("|%-30s" % i, end="")
        print(
            "\n------------------------------------------------------------------------------------------------------------------------------------------------------------",
            end="")
        s = ["", "", "", "", "", "", "", "", "", ""]
        cnt = 0
        for i in self.__menuList.keys():
            cnt = 0
            for j in range(len(self.__menuList[i])):
                cnt += 1

                s[cnt] += "| %-23s" % (self.__menuList[i][j].getName())
                s[cnt] += "%4s  " % (self.__menuList[i][j].getPrice())
            for j in range(
                    len(self.__menuList[i]) + 1,
                    len(self.__menuList['Tea']) + 1):
                s[j] += "|                              "

        for i in range(len(s)):
            print(s[i])


if __name__ == "__main__":
    m = MenuPrinter()
    m.Print()
