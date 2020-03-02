# 주문 안내 메세지 출력 및 주문받음
from com.kakao.cafe.module.menuPrinter import MenuPrinter
from com.kakao.cafe.cafe import *  #input을 어디서 받아야할지 모르겠음 cafe?
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

import re
import time  #시간 출력


class OrderTaker(MenuPrinter):
    def __init__(self):
        super().__init__()
        self.menuPrinter = MenuPrinter()
        self.__menuList = self.menuPrinter.getMenulist(
        )  #menuPrinter __menuList 받기
        self.__orderMenu = list()  # 메뉴, 개수, 옵션 결과리스트
        self._addList = dict()  #추가되는거 따로 정리 AddList dict에 정리
        self.countResult = list()  #숫자가 포함되어있으면 리스트에 넣는것
        self.matchResult = 0
        self.getOrdertime = list()  #선입선출하기 위한 날짜보기
        self.addCheck = list()  # 손님이 주문할 때 추가 또는 'add'가 포함되어있으면 확인
        self.addCheck.append('추가')
        self.addCheck.append('add')

        self.__addList['Ade'].append(LemonAde.addLemon())
        self.__addList['Ade'].append(OrangeAde.addOrange())
        self.__addList['Ade'].append(StrawberryAde.addStrawberry())
        self.__addList['Waffle'].append(
            BelgianWaffle.addWaffle())  # 와플만 더해지는거 생각해야됨. 가격때문에 못나눔
        self.__addList['Waffle'].append(FruitsWaffle.addWaffle())
        self.__addList['Waffle'].append(FruitsWaffle.addFruitsMango())
        self.__addList['Waffle'].append(FruitsWaffle.addFruitsStrawberry())
        self.__addList['Waffle'].append(FruitsWaffle.addBlueberry())
        self.__addList['Waffle'].append(IceWaffle.addWaffle())
        self.__addList['Waffle'].append(IceWaffle.addIceCream())
        self.__addList['Cake'].append(RedVelvetCheeseCake.addRedVelvetPowder())
        self.__addList['Cake'].append(TiramisuCake.addChocolatePowder())
        self.__addList['Coffee'].append(CafeMocha.addMocha())
        self.__addList['Coffee'].append(Cappuccino.addCinnamon())
        self.__addList['Coffee'].append(CaramelMacchiato.addCaramelSyrup())
        self.__addList['Coffee'].append(Espresso.addShot())
        self.__addList['Coffee'].append(Espresso.sizeUp())
        self.__addList['Coffee'].append(GreenTeaLatte.addCondensedMilk())
        self.__addList['Coffee'].append(Latte.addShot())
        self.__addList['Coffee'].append(VanillaLatte.addVanillaSyrup())
        self.__addList['Smoothie'].append(BerryBerrySmoothie.addBerry())
        self.__addList['Smoothie'].append(PineappleSmoothie.addPineapple())
        self.__addList['Smoothie'].append(YogurtSmoothie.addYogurt())
        self.__addList['Tea'].append(ChamomileTea.addChamomileTea())
        self.__addList['Tea'].append(GreenTea.addGreenTea())
        self.__addList['Tea'].append(HibiscusTea.addHibiscusTea())
        self.__addList['Tea'].append(IceTea.addPeachPowder())
        self.__addList['Tea'].append(MatchaMilkTea.addBlackTea())
        self.__addList['Tea'].append(MatchaMilkTea.addCondensedMilk())
        self.__addList['Tea'].append(MatchaMilkTea.addMatcha())
        self.__addList['Tea'].append(PeppermintTea.addPeppermintTea())
        self.__addList['Tea'].append(RooibosTea.addRooibosTea())
        self.__addList['Tea'].append(RoyalMilkTea.addBlackTea())
        self.__addList['Tea'].append(RoyalMilkTea.addRoyalHoney())

    def orderTaker(self, __menuList):
        print("-----주문 안내 메시지-----")
        self.ordertoCumstomer()
        self.time = self.getOrdertime()
        self.__orderMenu.append(self.time)  #시간 영수증 출력하기 위해서
        k = 0

        while (k != len(self._order)):  #반복을 줄이기 위해서 숫자부터 계산
            self.addmatchResult = self._order[k].find(self.addcheck)
            self.addcountResult = re.findall("\d",
                                             self._order[k])  #몇 개  숫자 있는지 확인

            if (len(self.addcountResult != 0)):  #담겨있으면 그 숫자를 int형해서 추가.
                self.__orderMenu[k - 1].append(int(
                    self._order[k]))  # 개수는 메뉴 주문 뒤에 오니까 둘이 리스트에 따로 담음
                self.count += 1
                break

            for i in self.__menuList.keys():  #Menu 찾기
                for j in self.__menuList.values():
                    if (self._order[k] == self.__menuList[i][j].getName()
                        ):  #getName과 주문이 같으면
                        self.__orderMenu[k].append(self._order[k])
                        k += 1
                        break
                    else:
                        continue

            if (addmatchResult != -1):  #추가 찾기
                for m in self.__addList.keys():
                    for n in self.__addList.values():
                        if (self._order[k] == self.__addList[m][n]):
                            self.__orderMenu.append(self.order[k])
                        else:
                            break

            else:
                print("주문을 다시해주세요")

    def ordertoCumstomer(self):  #손님에게 주문
        self._order = str(input())
        self._order = list(self._order)
        self._order = self._order.strip()
        return self._order

    def getMenulist(self) -> dict:  #MenuPrinter에서 menu담아옴
        return self.__menuList

    def getAddlist(self) -> dict:  #추가하는 것만 따로 모음. 나중에 값 계산할때 필요할것같아서.
        return self.__addList

    def getordertoCumstomer(self) -> list():  #손님이 주문한 거 출력
        return self._order

    def getOrderlist(
        self
    ) -> list:  #orderChecker에게 넘겨줄 뚜렷한 ex) 카라멜시럽 추가 -> addCaramelSyrup()으로
        return self.__orderMenu

    def getOrdertime(self) -> list:  #선입선출하기 위한 시간 출력
        self.orderTime.append(time.localtime())
        return self.orderTime


if __name__ == '__main__':
    test = OrderTaker()
    print(test.Order())
