from com.kakao.cafe.module.menuPrinter import MenuPrinter
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
        self.__orderMenu = list()  # OrderChecker에게 넘기위한 마지막 결과리스트
        self.__addList = dict(
        )  #메뉴에 추가옵션을 나누기위해서 'menu'key에 'add' 추가옵션 VALUE에 넣기
        self.__addnameList = dict()
        self.getOrdertime = list()  #선입선출하기 위한 날짜보기

        self.addcountResult = 0  #숫자가 포함되어있으면 리스트에 넣는것
        self.addmatchResult = 0  # 손님이 주문한 리스트에서 addCheck가 확인해서 존재하면 확인하는 addmatchresult
        self._amount = 1
        self.addCheck = list()  # 손님이 주문할 때 추가 또는 'add'가 포함되어있으면 확인
        self.addCheck.append('추가')
        self.addCheck.append('add')

        self.__addList['addLemon'] = list()
        self.__addList['addLemon'].append(
            LemonAde.addLemon(LemonAde(), self._amount))
        self.__addList['addOrange'] = list()
        self.__addList['addOrange'].append(
            OrangeAde.addOrange(OrangeAde(), self._amount))
        self.__addList['addStrawberry'] = list()
        self.__addList['addStrawberry'].append(
            StrawberryAde.addStrawberry(StrawberryAde(), self._amount))
        self.__addList['addBelgianWaffle'] = list()
        self.__addList['addBelgianWaffle'].append(
            BelgianWaffle.addWaffle(
                BelgianWaffle(),
                self._amount))  # 와플만 더해지는거 생각해야됨. getPrice때문에 못나눔
        self.__addList['addFruitsWaffle'] = list()
        self.__addList['addFruitsWaffle'].append(
            FruitsWaffle.addWaffle(FruitsWaffle(), self._amount))
        self.__addList['addFruitsMango'] = list()
        self.__addList['addFruitsMango'].append(
            FruitsWaffle.addFruitsMango(FruitsWaffle(), self._amount))
        self.__addList['addFruitsStrawberry'] = list()
        self.__addList['addFruitsStrawberry'].append(
            FruitsWaffle.addFruitsStrawberry(FruitsWaffle(), self._amount))
        self.__addList['addBlueberry'] = list()
        self.__addList['addBlueberry'].append(
            FruitsWaffle.addFruitsBlueberry(FruitsWaffle(), self._amount))
        self.__addList['addIceWaffle'] = list()
        self.__addList['addIceWaffle'].append(
            IceWaffle.addWaffle(IceWaffle(), self._amount))
        self.__addList['addIceCream'] = list()
        self.__addList['addIceCream'].append(
            IceWaffle.addIceCream(IceWaffle(), self._amount))
        self.__addList['addRedVelvetPowder'] = list()
        self.__addList['addRedVelvetPowder'].append(
            RedVelvetCheeseCake.addRedVelvetPowder(RedVelvetCheeseCake(),
                                                   self._amount))
        self.__addList['addChocolatePowder'] = list()
        self.__addList['addChocolatePowder'].append(
            TiramisuCake.addChocolatePowder(TiramisuCake(), self._amount))
        self.__addList['addMocha'] = list()
        self.__addList['addMocha'].append(
            CafeMocha.addMocha(CafeMocha(), self._amount))
        self.__addList['addCoinnamon'] = list()
        self.__addList['addCoinnamon'].append(
            Cappuccino.addCinnamon(Cappuccino(), self._amount))
        self.__addList['addCaramelSyrup'] = list()
        self.__addList['addCaramelSyrup'].append(
            CaramelMacchiato.addCaramelSyrup(CaramelMacchiato(), self._amount))
        self.__addList['addEspressoShot'] = list()
        self.__addList['addEspressoShot'].append(
            Espresso.addShot(Espresso(), self._amount))
        self.__addList['sizeUp'] = list()
        self.__addList['sizeUp'].append(
            Espresso.sizeUp(Espresso(), self._amount))
        self.__addList['addCondenseMilk'] = list()
        self.__addList['addCondenseMilk'].append(
            GreenTeaLatte.addCondensedMilk(GreenTeaLatte(), self._amount))
        self.__addList['addLatteShot'] = list()
        self.__addList['addLatteShot'].append(
            Latte.addShot(Latte(), self._amount))
        self.__addList['addVanilaSyrup'] = list()
        self.__addList['addVanilaSyrup'].append(
            VanillaLatte.addVanillaSyrup(VanillaLatte(), self._amount))
        self.__addList['addBerry'] = list()
        self.__addList['addBerry'].append(
            BerryBerrySmoothie.addBerry(BerryBerrySmoothie(), self._amount))
        self.__addList['addPineapple'] = list()
        self.__addList['addPineapple'].append(
            PineappleSmoothie.addPineapple(PineappleSmoothie(), self._amount))
        self.__addList['addYogurt'] = list()
        self.__addList['addYogurt'].append(
            YogurtSmoothie.addYogurt(YogurtSmoothie(), self._amount))
        self.__addList['addChamomileTea'] = list()
        self.__addList['addChamomileTea'].append(
            ChamomileTea.addChamomileTea(ChamomileTea(), self._amount))
        self.__addList['addGreenTea'] = list()
        self.__addList['addGreenTea'].append(
            GreenTea.addGreenTea(GreenTea(), self._amount))
        self.__addList['addHibiscusTea'] = list()
        self.__addList['addHibiscusTea'].append(
            HibiscusTea.addHibiscusTea(HibiscusTea(), self._amount))
        self.__addList['addPeachPowder'] = list()
        self.__addList['addPeachPowder'].append(
            IceTea.addPeachPowder(IceTea(), self._amount))
        self.__addList['addBlackTea'] = list()
        self.__addList['addBlackTea'].append(
            MatchaMilkTea.addBlackTea(MatchaMilkTea(), self._amount))
        self.__addList['addCondenseMilk'] = list()
        self.__addList['addCondenseMilk'].append(
            MatchaMilkTea.addCondensedMilk(MatchaMilkTea(), self._amount))
        self.__addList['addMatcha'] = list()
        self.__addList['addMatcha'].append(
            MatchaMilkTea.addMatcha(MatchaMilkTea(), self._amount))
        self.__addList['addPeppermintTea'] = list()
        self.__addList['addPeppermintTea'].append(
            PeppermintTea.addPeppermintTea(PeppermintTea(), self._amount))
        self.__addList['addRooibosTea'] = list()
        self.__addList['addRooibosTea'].append(
            RooibosTea.addRooibosTea(RooibosTea(), self._amount))
        self.__addList['addBlackTea'] = list()
        self.__addList['addBlackTea'].append(
            RoyalMilkTea.addBlackTea(RoyalMilkTea(), self._amount))
        self.__addList['addRoyalHoney'] = list()
        self.__addList['addRoyalHoney'].append(
            RoyalMilkTea.addRoyalHoney(RoyalMilkTea(), self._amount))

        self.__addnameList['Add'] = list()
        self.__addnameList['Add'].append('addWaffle')
        self.__addnameList['Add'].append('addOrange')
        self.__addnameList['Add'].append('addStrawberry')
        self.__addnameList['Add'].append('addFruitsMango')
        self.__addnameList['Add'].append('addFruitsStrawberry')
        self.__addnameList['Add'].append('addBlueberry')
        self.__addnameList['Add'].append('addIceCream')
        self.__addnameList['Add'].append('addRedVelvetPowder')
        self.__addnameList['Add'].append('addChocolatePowder')
        self.__addnameList['Add'].append('addMocha')
        self.__addnameList['Add'].append('addCinnamon')
        self.__addnameList['Add'].append('addCaramelSyrup')
        self.__addnameList['Add'].append('addShot')
        self.__addnameList['Add'].append('sizeUp')
        self.__addnameList['Add'].append('addCondenseMilk')
        self.__addnameList['Add'].append('addVanillaSyrup')
        self.__addnameList['Add'].append('addBerry')
        self.__addnameList['Add'].append('addPineapple')
        self.__addnameList['Add'].append('addYogurt')
        self.__addnameList['Add'].append('addChamomileTea')
        self.__addnameList['Add'].append('addGreenTea')
        self.__addnameList['Add'].append('addHibiscusTea')
        self.__addnameList['Add'].append('addPeachPowder')
        self.__addnameList['Add'].append('addBlackTea')
        self.__addnameList['Add'].append('addCondenseMilk')
        self.__addnameList['Add'].append('addMatcha')
        self.__addnameList['Add'].append('addPeppermintTea')
        self.__addnameList['Add'].append('addRooibosTea')
        self.__addnameList['Add'].append('addBlackTea')
        self.__addnameList['Add'].append('addRoyalHoney')

    def orderTaker(self, _order) -> list:
        print("-----주문 안내 메시지-----")
        self._order = _order
        #self.ordertoCumstomer()  # 손님에게 주문받는다.
        #self.time = self.getOrdertime()  #시간을 측정한다.
        #self.__orderMenu.append(self.time)  #맨 첫번째 시간을 넣는다. 영수증 출력할때 시간이 필요하기 때문에
        k = 0  #반복하기 위한 변수

        while (k != len(self._order)):  # 주문의 길이만큼 돌린다.
            #완료
            self._order[k] = self._order[k].lower()
            for i in range(len(self.addCheck)):
                self.addmatchResult = self._order[k].find(
                    self.addCheck[i])  #'add' 또는 '추가'가 있으면 0을반환하고 아니면 -1을 반환한다.
                if (addmatchResult == 0):  # 0이면
                    for m in self.__addnameList.values():  #
                        m = m.lower()
                        if (self._order[k] == m):
                            for n in self.__addList.keys():
                                n = n.lower()
                                if (n == m):
                                    self.__orderMenu.append(self.order[k])
                                else:
                                    continue
                        else:
                            continue
                else:
                    continue
            #완료
            self.addcountResult = re.findall(
                "\d+", self._order[k])  # %d+(숫자로 하나이상 된)로 된 숫자가 있는지 판별한다.
            if (len(self.addcountResult != 0)):
                self.__orderMenu.append(self.addcountResult)

            #완료
            for i in self.__menuList.keys():  #Menu 찾기 한글도 구별해야함.
                for j in self.__menuList.values():
                    self.matchmenuList = self.__menuList[i][j].getName().lower
                    if (self._order[k] == self.matchmenuList
                        ):  #getName과 주문이 같으면
                        self.__orderMenu[k].append(self._order[k])
                        break
                    else:
                        continue

            return self.__orderMenu

    '''
    def ordertoCumstomer(self) -> list:  #손님에게 주문
        self._order = input().split()  #문자열 리스트로 받는다.
        #self._order = self._order.strip() 공백제거
        # self._order = self._order.lower() 리스트는 소문자로 못바꿈
        return self._order
    '''

    def getMenulist(self) -> dict:  #MenuPrinter에서 menu담아옴
        return self.__menuList

    def getAddlist(self) -> dict:  #추가하는 것만 따로 모음. 나중에 값 계산할때 필요할것같아서.
        return self.__addList

    def getordertoCumstomer(self, _order) -> list():  #손님이 주문한 거 출력
        self._order = _order
        return self._order

    def getOrderlist(
        self
    ) -> list:  #orderChecker에게 넘겨줄 뚜렷한 ex) 카라멜시럽 추가 -> addCaramelSyrup()으로
        return self.__orderMenu

    def getOrdertime(self) -> list:  #선입선출하기 위한 시간 출력
        self.orderTime.append(time.localtime())
        return self.orderTime
