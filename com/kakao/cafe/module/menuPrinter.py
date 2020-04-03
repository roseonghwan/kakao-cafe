#-*- coding:utf-8 -*-
from __future__ import print_function, absolute_import
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

        # self.__menuList를 dict() 자료형으로 선언,
        # value 값은 본 클래스 내에있는 getEspresso(), getAde(), getSmoothie(), getTea(), getDessert() method로 가져옴
        self.__menuList = dict()
        self.__menuList['Espresso'] = self.getEspresso()
        self.__menuList['Ade'] = self.getAde()
        self.__menuList['Smoothie'] = self.getSmoothie()
        self.__menuList['Tea'] = self.getTea()
        self.__menuList['Dessert'] = self.getDessert()

    # self.__menuList를 dict 형태로 가져오는 method
    def getMenulist(self) -> dict:
        return self.__menuList

    # Espresso 객체들을 list 형태로 가져오는 method
    def getEspresso(self) -> list:
        return [
            Espresso(),
            Americano(),
            Latte(),
            GreenTeaLatte(),
            VanillaLatte(),
            CafeMocha(),
            Cappuccino(),
            CaramelMacchiato()
        ]

    # Ade 객체들을 list 형태로 가져오는 method
    def getAde(self) -> list:
        return [LemonAde(), OrangeAde(), StrawberryAde()]

    # Smoothie 객체들을 list 형태로 가져오는 method
    def getSmoothie(self) -> list:
        return [YogurtSmoothie(), BerryBerrySmoothie(), PineappleSmoothie()]

    # Tea 객체들을 list 형태로 가져오는 method
    def getTea(self) -> list:
        return [
            ChamomileTea(),
            GreenTea(),
            HibiscusTea(),
            IceTea(),
            LavenderTea(),
            RoyalMilkTea(),
            MatchaMilkTea(),
            PeppermintTea(),
            RooibosTea()
        ]

    # Dessert 객체들을 list 형태로 가져오는 method
    def getDessert(self) -> list:
        return [
            BelgianWaffle(),
            FruitsWaffle(),
            IceWaffle(),
            NewYorkCheeseCake(),
            RainbowCheeseCake(),
            RedVelvetCheeseCake(),
            TiramisuCake()
        ]

    # cafeMenu에 포함된 객체들을 list 형태로 가져오는 method
    def getMenu(self) -> list:
        return self.getEspresso() + self.getAde() + self.getSmoothie(
        ) + self.getTea() + self.getDessert()

    # CafeMenu를 Print하는 method 132 ~ 136번째 줄 참고!
    def Print(self) -> None:

        print("Wellcome to Kakao Cafe!!")  # Print #1
        print("-" * 156)  # Print #2
        for category in self.__menuList:
            print("|%-30s" % category, end="")  # Print #3
        print("\n" + "-" * 156)  # Print #4

        # make #5 메뉴를 한줄씩 출력
        s = ["", "", "", "", "", "", "", "", "", ""]
        num = 1
        for i in self.__menuList.keys():
            cnt = 0
            for j in range(len(self.__menuList[i])):
                cnt += 1
                s[cnt] += "|%-2s" % (str(num)) + " %-22s" % (
                    self.__menuList[i][j].getName())  # s 배열에 cafeMenu들의 이름을 저장
                s[cnt] += "%4s " % (self.__menuList[i][j].getPrice()
                                    )  # s 배열에 cafeMenu들의 가격을 저장
                num += 1
            for j in range(
                    len(self.__menuList[i]) + 1,
                    len(self.__menuList['Tea']) + 1):  # s 배열에 빈칸 만들기
                s[j] += "|" + " " * 30

        for i in range(len(s)):
            print(s[i])  # Print #5


"""
(#1) Wellcome to Kakao Cafe!!
(#2) ------------------------------------------------------------------------------------------------------------------------------------------------------------
(#3) |Espresso                      |Ade                           |Smoothie                      |Tea                           |Dessert                       
(#4) ------------------------------------------------------------------------------------------------------------------------------------------------------------
(#5) |1  Espresso              2500 |9  LemonAde              3500 |12 YogurtSmoothie        5000 |15 ChamomileTea          3500 |24 BelgianWaffle         5000 
     |2  Americano             3000 |10 OrangeAde             3500 |13 BerryBerrySmoothie    5000 |16 GreenTea              3000 |25 FruitsWaffle          6000  
     |3  Latte                 4000 |11 StrawberryAde         3500 |14 PineappleSmoothie     5000 |17 HibiscusTea           3000 |26 IceWaffle             6000 
     |4  GreenTeaLatte         4500 |                              |                              |18 IceTea                3000 |27 NewYorkCheeseCake     5000 
     |5  VanillaLatte          4000 |                              |                              |19 LavenderTea           3500 |28 RainbowCheeseCake     5500 
     |6  CafeMocha             4000 |                              |                              |20 RoyalMilkTea          5000 |29 RedVelvetCheeseCake   6000 
     |7  Cappuccino            4500 |                              |                              |21 MatchaMilkTea         4500 |30 TiramisuCake          5500  
     |8  CaramelMacchiato      4000 |                              |                              |22 PeppermintTea         3500 |                              
     |                              |                              |                              |23 RooibosTea            4500 |                              
"""