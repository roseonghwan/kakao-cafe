# 주문 안내 메세지 출력 및 주문받음
#-*- coding:utf-8 -*-
from __future__ import print_function, absolute_import
from com.kakao.cafe.module.menuPrinter import MenuPrinter  #MenuPrinter에 있는 menuList를 가져오기 위해서
from com.kakao.cafe.module.cafeWorker import CafeWorker
import time  #영수증 출력할 때 주문시간을 나오게 하기 위해서 5번
import itertools
'''
0. 중요한건 메인모듈에서 인스턴스화해서 내게 넣어주기 때문에
   내가 모든걸 import하거나 인스턴스화를 할 필요가 없다. <완료>
1. 손님에게 메뉴리스트에 있는 숫자만을 입력해달라고 한다.(숫자를 입력하고 에러가 나면 다시 주문해달라고 함) <완료>
2. MenuPrinter에서 받은 리스트와 손님에게 받은 숫자를 비교한다. <완료>
3. 비교한게 같으면 그 메뉴에 대한 수량을 묻고 추가 옵션에 대해서 나온다.(동시에 시간(선입선출하기 위해서)과 총 가격을 출력하기 위해서 Price까지 받는다.)
3-1. 공통적으로 되는 추가옵션들을 메소드로 만들어 좀 더 간편하게 한다. <완료>
3-2  추가옵션에 관해서도 물어볼 때 해당되는 정답이 안나오면 다시 주문할 수 있도록 한다. <완료>
4. 손님이 선택한 항목을 OrderList에 차례대로 입력해준다. <완료>
4-1 orderList에 추가옵션을 더해준다. <완료>
5. 4번 항목인 paymentManager에게 allPrice(총가격)을 주기 위해서 함수를 제공한다. <완료>
6. getOrderList는 5번 receiptPrinter에게 줄 품목, 수량을 주기위함, 함수를 편히 제공하기 위해 선언한다. <완료>
6-1 receiptPrinter는 영수증에서 날짜를 출력하기 때문에 주문하는 즉시 시간을 나타낼 수 있도록 한다.
6-2 리스트에 넣어서 getter를 만들어준다.
** self.orderList 예제 : ['Espresso', '2', 'addShot', 2, 'newYorkCheeseCake']
'''


class OrderTaker(CafeWorker):
    def __init__(self):
        self.orderlist = []  #멤버변수 orderList 최종적으로 넘겨줄 리스트
        self.__allPrice = int()  #총 가격을 더할 멤버 변수
        self.addList = []  #
        self.menulist = list()
        self.results = list()

    def Print(self) -> None:
        print("---------------주문 안내 메시지---------------")
        print("---메뉴 리스트에 나와있는 숫자를 입력해주세요---")

    def takeOrder(self, menuList) -> list:  #손님에게 주문을 받는 함수 takeOrder
        #메뉴리스트에 있는 숫자까지 입력해야되는 걸 구분해야됨.
        self.__allPrice = 0  #주문을 할 때 마다 총 가격을 0으로 초기화해준다.
        #손님이 주문한 번호와 같은지 판별헤서 같으면 메뉴에 관한 옵션을 출력함.
        for Length in range(len(menuList)):  #손님에게 주문받은 ordertoCustmore만큼 반복
            #손님이 주문한 번호를 간략하게 바꿔놓는다.
            self.addList = []  # 돌아 왔을 때 다시 초기화
            number = menuList[Length]
            #에스프레소
            if number == 1:
                self.addName(number - 1)  #orderlist에 getName추가 [['Espresso']]
                self.askAmount()  #수량 확인 [['Espresso', 1]]
                self.addAllPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.confirmHot()  #에스프레소는 뜨거운것 밖에 안되기 때문에 HOT 확정
                    self.askAddshot()  #샷 추가 확인
                    self.askSizeUp()  #사이즈업 확인
                #에스프레소는 차갑게 먹을 수 없으므로 askIced 메소드를 물어볼 필요 없음
            #아메리카노 - 에스프레스 상속
            elif number == 2:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()  #Iced확인
                    self.askAddshot()  #샷 추가 확인
                    self.askSizeUp()  #사이즈업 확인

            #라떼 - 에스프레스 상속
            elif number == 3:
                self.addName(number - 1)
                self.askAmount()  #수량 확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()  #Iced확인
                    self.askAddshot()  #샷 추가 확인
                    self.askSizeUp()  #사이즈업 확인
            #그린티라떼 - 라떼 상속
            elif number == 4:
                self.addName(number - 1)
                self.askAmount()  #수량 확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askAddshot()  #샷 추가 확인
                    self.askSizeUp()  #사이즈업 확인
                    self.askGreenTea()  #GreenTea 추가 확인
                    self.askCondensedMilk()  #연유 추가 확인
            #바닐라라떼 - 라떼 상속
            elif number == 5:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askAddshot()  #샷 추가 확인
                    self.askSizeUp()  #사이즈업 확인
                    self.askVanillaSyrup()  #바닐라 시업 추가 확인
            #카페모카 - 라떼 상속
            elif number == 6:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askAddshot()  #샷 추가 확인
                    self.askSizeUp()  #사이즈업 확인
                    self.askCafeMocha()  #모카 추가 확인
            #카푸치노 - 라떼 상속
            elif number == 7:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askAddshot()  #샷 추가 확인
                    self.askSizeUp()  #사이즈업 확인
                    self.askCinnamon()  #시나몬 추가 확인
            #카라멜마끼야또 - 라떼 상속
            elif number == 8:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askAddshot()  #샷 추가 확인
                    self.askSizeUp()  #사이즈업 확인
                    self.askCaramelSyrup()  #카라멜시럽 추가 확인
            #레몬에이드
            elif number == 9:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.confirmIce()
                    self.askLemon()  # 레몬 추가 확인
            #오렌지에이드
            elif number == 10:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.confirmIce()
                    self.askOrange()  # 오렌지 추가 확인
            #딸기에이드
            elif number == 11:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.confirmIce()
                    self.askStrawberry()  # 딸기 추가 확인
            #요거트스무디
            elif number == 12:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.confirmIce()
                    self.askYogurt()  #요거트 추가 확인
            #블루베리스무디
            elif number == 13:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.confirmIce()
                    self.askBerry()  #블루베리 추가 확인
            #파인애플스무디
            elif number == 14:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.confirmIce()
                    self.askPineapple()  #파인애플 추가 확인
            #카모마일 차
            elif number == 15:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.confirmIce()
                    self.askChamomileTea()  #카모마일 추가 확인
            #그린티
            elif number == 16:
                self.addName(number)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askGreenTea(
                    )  #그린티추가 그린티 라떼도 있으므로 getPrice가 다를 시 분류해줘야함.
            #히비스커스 티
            elif number == 17:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askHibiscusTea()  #카모마일 추가 확인
            #아이스티
            elif number == 18:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.confirmIce()
                    self.askPeachPowder()  #복숭아 파우더 추가 확인
            #라벤더 티
            elif number == 19:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askLavenderTea()  #라벤더 추가 확인
            #로얄밀크 티
            elif number == 20:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askBlackTea()  #블랙티 추가 확인
                    self.askRoyalHoney()  #꿀 추가 확인
            #맛차 밀크 티
            elif number == 21:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askBlackTea()  #블랙티 추가 확인
                    self.askCondensedMilk()  #연유 추가 확인
            #페퍼민트 티
            elif number == 22:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askPeppermintTea()  #페퍼민트 티 추가 확인
            #루이보스 티
            elif number == 23:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askIceOrHot()
                    self.askRooibosTea()  #루이보스 티 추가 확인
            #벨기안 와플
            elif number == 24:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askWaffle()  #와플 추가
            #과일 와플
            elif number == 25:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askWaffle()  #와플 추가
                    self.askFruitsMango()  #망고 추가 확인
                    self.askFruitsStrawberry()  #딸기 추가 확인
                    self.askFruitsBlueberry()  # 블루베리 추가 확인
            #아이스크림 와플
            elif number == 26:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askWaffle()  #와플 추가
                    self.askIceCream()  #아이스크림 추가
            #뉴욕치즈케이크~
            elif number == 27:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
            #무지개치즈케이크
            elif number == 28:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
            #레드벨벳치즈케이크
            elif number == 29:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askRedVelvetPowder()  #레드벨벳 파우더 추가 확인
            #티라미수 케이크
            elif number == 30:
                self.addName(number - 1)
                self.askAmount()  #수량확인
                self.addAllPrice(number - 1)  # 총 가격을 구하기위해 수량을 넣어줌
                for i in range(self.addList[1]):
                    self.askChocolatePowder()  #초콜릿 파우더 확인
            else:
                print(" E R R O R ")
            self.orderlist.append(self.addList)
        return self.orderlist

    #orderList에 메뉴를 추가하는 매소드
    #Menu는 MenuPrinter에 있는 객체들을 나누기 위해서 사용함. 손님에게 받은 수
    #중간중간 Menu를 따로 빼주는 거는 메뉴마다 리스트가 서로 달리 존재하기 때문에
    #그 전의 리스트 Length만큼 빼주는 것이다.
    #<완료>
    def addName(self, Menu: int) -> list:
        if Menu <= 7:  # 1~8 에스프레스
            self.addList.append(MenuPrinter().getEspresso()[Menu].getName())
        elif Menu <= 10:
            Menu -= 8  # 9~11 에이드
            self.addList.append(MenuPrinter().getAde()[Menu].getName())
        elif Menu <= 13:
            Menu -= 11  # 12~14 스무디
            self.addList.append(MenuPrinter().getSmoothie()[Menu].getName())
        elif Menu <= 22:
            Menu -= 14  # 15~ 23 티
            self.addList.append(MenuPrinter().getTea()[Menu].getName())
        else:
            Menu -= 23  # 24 ~ 30 디저트
            self.addList.append(MenuPrinter().getDessert()[Menu].getName())
        #return으로 self.addList를 해줌.
        return self.addList

    #수량을 질문하는 메소드
    #손님에게 묻는 수량이 int(정수형이 아니면) 에러나게 해야함.
    #<완료>
    def askAmount(self) -> list:
        try:
            print("수량을 입력해주세요 : ")
            amount = int(input())
            self.addList.append(amount)  #리스트에 수량을 추가함. 메뉴 다음에 있으면 편함.
        except Exception:
            print("수량을 다시 입력해주세요 ")
        return self.addList

    def addAllPrice(self, price: int) -> list:
        if price <= 7:  # 1~8 에스프레스
            self.__allPrice = self.__allPrice + (
                MenuPrinter().getEspresso()[price].getPrice() *
                self.addList[1])
        elif price <= 10:
            price -= 8  # 9~11 에이드
            self.__allPrice = self.__allPrice + (
                MenuPrinter().getAde()[price].getPrice() * self.addList[1])
        elif price <= 13:
            price -= 11  # 12~14 스무디
            self.__allPrice = self.__allPrice + (
                MenuPrinter().getSmoothie()[price].getPrice() *
                self.addList[1])
        elif price <= 22:
            price -= 14  # 15~ 23 티
            self.__allPrice = self.__allPrice + (
                MenuPrinter().getTea()[price].getPrice() * self.addList[1])
        else:
            price -= 23  #24 ~ 30 디저트
            self.__allPrice = self.__allPrice + (
                MenuPrinter().getDessert()[price].getPrice() * self.addList[1])
        return self.__allPrice

    #------------------------------Add Options--------------------------
    #샷을 질문하는 메소드
    #<완료>
    def askAddshot(self) -> list:
        while (True):
            try:
                print("삿을 추가하시거나 빼시겠습니까? 추가하거나 빼면 : True 기본 : 'False'")
                self.askShot = str(input())
                #샷을 추가하거나 빼면 어떻게 할지 물어본다.
                if self.askShot == 'True':
                    print("샷 추가 : 'True' 샷 빼기 : 'False'")
                    while (True):
                        self.Shot = str(input())
                        if self.Shot == 'True':  #샷 추가
                            self.addList.append('addShot')
                            print("샷 추가를 얼마나 하시겠습니까? ")
                            self.addShot = int(input())
                            self.addList.append(int(self.addShot))
                            self.__allPrice = self.__allPrice + (int(
                                self.addShot * 500))
                            break
                        elif self.Shot == 'False':
                            self.addList.append('subShot')
                            print("샷을 얼마나 빼시겠습니까? ")
                            self.subShot = int(input())
                            self.addList.append(int(self.subShot))
                            self.__allPrice = self.__allPrice - (int(
                                self.subShot * 500))
                            break
                        else:
                            raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                            continue
                #샷을 기본으로 하면 pass한다.
                elif self.askShot == False:
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #hot or ice를 물어보는 메소드
    def askIceOrHot(self) -> list:
        while (True):
            try:
                print("ICE는 True HOT는 False로 입력해주십시오 ")
                self.ice = str(input())
                if self.ice == 'True':
                    self.addList.append('ICE')
                    break
                elif self.ice == 'False':
                    self.addList.append('HOT')
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    def confirmIce(self) -> None:
        self.addList.append('ICE')

    def confirmHot(self) -> None:
        self.addList.append('HOT')

    #사이즈 추가 Espresson method
    def askSizeUp(self) -> list:
        while (True):
            try:
                print("사이즈를 추가하시겠습니까? 추가 : True 기본 : False")
                self.sizeup = str(input())
                if self.sizeup == 'True':
                    self.addList.append("sizeUp")
                    print("Grande : 'True' , Venti : False")
                    self.Choose = str(input())
                    if self.Choose == 'True':
                        self.addList.append('Grande')
                        self.__allPrice = self.__allPrice + 500
                        break
                    elif self.Choose == 'False':
                        self.addList.append('Venti')
                        self.__allPrice = self.__allPrice + 500
                        break
                    else:
                        raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                        continue
                elif self.sizeup == 'False':
                    pass
                    break
                else:
                    raise Exception("다시 입력해주십시오")
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #GreenTea add Option 16 GreenTea
    def askGreenTea(self):
        while (True):
            try:
                print("그린티를 추가하시겠습니까? 추가 : 'True' 기본 : 'False'")
                self.addGreenTea = str(input())
                if self.addGreenTea == 'True':
                    self.addList.append('addGreenTea')
                    print("얼만큼 추가하시겠습니까? ")
                    self.addGreenTea = int(input())
                    self.addList.append(int(self.addGreenTea))
                    self.__allPrice = self.__allPrice + int(
                        self.addGreenTea) * 300
                    break
                elif self.addGreenTea == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
        return self.addList

    #GreenTea condenseMilk Option
    def askCondensedMilk(self):
        while (True):
            try:
                print("연유 추가하시겠습니까? 추가 : 'True' 기본 : 'False'")
                self.addMilk = str(input())
                if self.addMilk == 'True':
                    self.addList.append("addCondensedMilk")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addMilk = int(input())
                    self.addList.append(int(self.addMilk))
                    self.__allPrice = self.__allPrice + (int(self.addMilk) *
                                                         300)
                    break
                elif self.addMilk == 'False':
                    pass
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #VanillaLatte Option
    def askVanillaSyrup(self):
        while (True):
            try:
                print("바닐라 시럽 추가하시겠습니까? 추가 : 'True' 기본 : 'False'")
                self.addSyrup = str(input())
                if self.addSyrup == 'True':
                    self.addList.append('addVanillaSyrup')
                    print("얼만큼 추가하시겠습니까? ")
                    self.addSyrup = int(input())
                    self.addList.append(int(self.addSyrup))
                    self.__allPrice = self.__allPrice + (int(self.addSyrup) *
                                                         200)
                    break
                elif self.addSyrup == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #CafeMocha 카페모카 추가 옵션
    def askCafeMocha(self):
        while (True):
            try:
                print("모카 추가하시겠습니까? 추가 : 'True' 기본 : 'False'")
                self.addMocha = str(input())
                if self.addMocha == 'True':
                    self.addList.append('addCafeMocha')
                    print("얼만큼 추가하시겠습니까? ")
                    self.addMocha = int(input())
                    self.addList.append(int(self.addMocha))
                    self.__allPrice = self.__allPrice + (int(self.addMocha) *
                                                         300)
                    break
                elif self.addMocha == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #Cappuccino 카푸치노 추가 옵션
    def askCinnamon(self):
        while (True):
            try:
                print("시나몬 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addCinnamon = str(input())
                if self.addCinnamon == 'True':
                    self.addList.append('addCinnamon')
                    print("얼만큼 추가하시겠습니까? ")
                    self.addCinnamon = int(input())
                    self.addList.append(int(self.addCinnamon))
                    self.__allPrice = self.__allPrice + self.addCinnamon  #약간 이상한느낌이 들음....  + amount?
                    break
                elif self.addCinnamon == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #CaramelMacchiato
    def askCaramelSyrup(self):
        while (True):
            try:
                print("카라멜 시럽 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addSyrup = str(input())
                if self.addSyrup == 'True':
                    self.addList.append('addCaramelSyrup')
                    print("얼만큼 추가하시겠습니까? ")
                    self.addSyrup = int(input())
                    self.addList.append(int(self.addSyrup))
                    self.__allPrice = self.__allPrice + (int(self.addSyrup) *
                                                         200)
                    break
                elif self.addSyrup == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #LemonAde 레몬에이드 레몬추가 addOption
    def askLemon(self):
        while (True):
            try:
                print("레몬 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addLemon = str(input())
                if self.addLemon == 'True':
                    self.addList.append('addLemon')
                    print("얼만큼 추가하시겠습니까? ")
                    self.addLemon = int(input())
                    self.addList.append(int(self.addLemon))
                    self.__allPrice = self.__allPrice + (int(self.addLemon) *
                                                         500)
                    break
                elif self.addLemon == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    def askOrange(self):
        while (True):
            try:
                print("오렌지 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addOrange = str(input())
                if self.addOrange == 'True':
                    self.addList.append('addOrange')
                    print("얼만큼 추가하시겠습니까? ")
                    self.addOrange = int(input())
                    self.addList.append(int(self.addOrange))
                    self.__allPrice = self.__allPrice + (int(self.addOrange) *
                                                         500)
                    break
                elif self.addOrange == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #StrawberryAde 딸기 추가
    def askStrawberry(self):
        while (True):
            try:
                print("딸기 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addStrawberry = str(input())
                if self.addStrawberry == 'True':
                    self.addList.append('addStrawberry')
                    print("얼만큼 추가하시겠습니까? ")
                    self.addStrawberry = int(input())
                    self.addList.append(int(self.addStrawberry))
                    self.__allPrice = self.__allPrice + (
                        int(self.addStrawberry) * 500)
                    break
                elif self.addStrawberry == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #YogurtSmoothie 요거트 추가
    def askYogurt(self):
        while (True):
            try:
                print("요거트 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addYogurt = str(input())
                if self.addYogurt == 'True':
                    self.addList.append('addYogurt')
                    print("얼만큼 추가하시겠습니까? ")
                    self.addYogurt = int(input())
                    self.addList.append(int(self.addYogurt))
                    self.__allPrice = self.__allPrice + (int(self.addYogurt) *
                                                         500)
                    break
                elif self.addYogurt == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #BerryBerrySmoothie 요거트 추가
    def askBerry(self):
        while (True):
            try:
                print("베리 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addBerry = str(input())
                if self.addBerry == 'True':
                    self.addList.append('addBerry')
                    print("얼만큼 추가하시겠습니까? ")
                    self.addBerry = int(input())
                    self.addList.append(int(self.addBerry))
                    self.__allPrice = self.__allPrice + (int(self.addBerry) *
                                                         500)
                    break
                elif self.addBerry == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #PineappleSmoothie 파인애플 추가
    def askPineapple(self):
        while (True):
            try:
                print("파인애플 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addPineapple = str(input())
                if self.addPineapple == 'True':
                    self.addList.append("addPineapple")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addPineapple = int(input())
                    self.addList.append(int(self.addPineapple))
                    self.__allPrice = self.__allPrice + (
                        int(self.addPineapple) * 500)
                    break
                elif self.addPineapple == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #ChamomileTea 카모마일 차
    def askChamomileTea(self):
        while (True):
            try:
                print("카모마일을 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addChamomileTea = str(input())
                if self.addChamomileTea == 'True':
                    self.addList.append("addChamomileTea")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addChamomileTea = int(input())
                    self.addList.append(int(self.addChamomileTea))
                    self.__allPrice = self.__allPrice + (
                        int(self.addChamomileTea) * 500)
                    break
                elif self.addChamomileTea == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #HibiscusTea 히비스커스 티?
    def askHibiscusTea(self):
        while (True):
            try:
                print("히비스커스을 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addHibiscusTea = str(input())
                if self.addHibiscusTea == 'True':
                    self.addList.append("addHibiscusTea")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addHibiscusTea = int(input())
                    self.addList.append(int(self.addHibiscusTea))
                    self.__allPrice = self.__allPrice + (
                        int(self.addHibiscusTea) * 500)
                    break
                elif self.addHibiscusTea == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #Icetea 피치파우더
    def askPeachPowder(self):
        while (True):
            try:
                print("복숭아 파우더를 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addPeachPowder = str(input())
                if self.addPeachPowder == 'True':
                    self.addList.append("addPeachPowder")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addPeachPowder = int(input())
                    self.addList.append(int(self.addPeachPowder))
                    self.__allPrice = self.__allPrice + (
                        int(self.addPeachPowder) * 400)
                    break
                elif (self.addPeachPowder == 'False'):
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #LavenderTea
    def askLavenderTea(self):
        while (True):
            try:
                print("라벤더를 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addLavenderTea = str(input())
                if self.addLavenderTea == 'True':
                    self.addList.append("addLavenderTea")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addLavenderTea = int(input())
                    self.addList.append(int(self.addLavenderTea))
                    self.__allPrice = self.__allPrice + (
                        int(self.addLavenderTea) * 500)
                    break
                elif (self.addLavenderTea == 'False'):
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #RoyalMilkTea BlackTea
    def askBlackTea(self) -> int:
        while (True):
            try:
                print("블랙티를 추가하시거나 빼시겠습니까? 추가하거나 빼면 : 'True' 기본 : 'False'")
                self.BlackTea = str(input())
                #블랙티을 추가하거나 빼면 어떻게 할지 물어본다.
                if self.BlackTea == 'True':
                    print("블랙티 추가 : 'True' 블랙티 빼기 : 'False'")
                    self.BlackTea = str(input())
                    if (self.BlackTea == 'True'):  #블랙티 추가
                        self.addList.append('addBlackTea')
                        print("블랙티 추가를 얼마나 하시겠습니까? ")
                        self.addBlackTea = int(input())
                        self.addList.append(int(self.addBlackTea))
                        self.__allPrice = self.__allPrice + (
                            int(self.addBlackTea) * 500)
                        break
                    elif (self.BlackTea == 'False'):
                        self.addList.append('subBlackTea')
                        print("블랙티을 얼마나 빼시겠습니까? ")
                        self.subBlackTea = int(input())
                        self.addList.append(int(self.subBlackTea))
                        self.__allPrice = self.__allPrice - int(
                            self.subBlackTea)
                        break
                    else:
                        raise Exception("True 또는 False로 입력해주시기 바랍니다.")
                        continue
                #블랙티을 기본으로 하면 pass한다.
                elif self.askBlackTea == 'False':
                    pass
                    break
                else:
                    raise Exception("True 또는 False로 입력해주시기 바랍니다.")
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #royalMilkTea addRoyalHoney
    def askRoyalHoney(self):
        while (True):
            try:
                print("꿀을 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addRoyalHoney = str(input())
                if self.addRoyalHoney == 'True':
                    self.addList.append("addRoyalHoney")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addRoyalHoney = int(input())
                    self.addList.append(int(self.addRoyalHoney))
                    self.__allPrice = self.__allPrice + (
                        int(self.addRoyalHoney) * 1000)
                    break
                elif self.addRoyalHoney == 'False':
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #addMatcha matchaMilkTea
    def askMatcha(self):
        while (True):
            try:
                print("말차를 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addMatcha = str(input())
                if self.addMatcha == 'True':
                    self.addList.append("addMatcha")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addMatcha = int(input())
                    self.addList.append(int(self.addMatcha))
                    self.__allPrice = self.__allPrice + (int(self.addMatcha) *
                                                         400)
                    break
                elif self.addMatcha == 'False':
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #addPeppermintTea  peppermintTea
    def askPeppermintTea(self):
        while (True):
            try:
                print("페퍼민트를 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addPeppermintTea = str(input())
                if self.addPeppermintTea == 'True':
                    self.addList.append("addPeppermintTea")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addPeppermintTea = int(input())
                    self.addList.append(int(self.addPeppermintTea))
                    self.__allPrice = self.__allPrice + (
                        int(self.addPeppermintTea) * 500)
                    break
                elif self.addPeppermintTea == 'False':
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #addRooibosTea rooibosTea
    def askRooibosTea(self):
        while (True):
            try:
                print("루이보스를 추가하시겠습니까? 추가 : 'True' 기본 : 'False'\n")
                self.addRooibosTea = str(input())
                if self.addRooibosTea == 'True':
                    self.addList.append("addRooibosTea")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addRooibosTea = int(input())
                    self.addList.append(int(self.addRooibosTea))
                    self.__allPrice = self.__allPrice + (
                        int(self.addRooibosTea) * 700)
                    break
                elif self.addRooibosTea == 'False':
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #def addWaffle beiganWaffle FruitsWaffle
    def askWaffle(self):
        while (True):
            try:
                print("와플을 추가하시겠습니까? 추가 : 'True' 거부 : 'False'\n")
                self.addWaffle = str(input())
                if self.addWaffle == 'True':
                    self.addList.append("addWaffle")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addWaffle = int(input())
                    self.addList.append(int(self.addWaffle))
                    self.__allPrice = self.__allPrice + (int(self.addWaffle) *
                                                         1000)
                    break
                elif self.addWaffle == 'False':
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #def addFruitsMango
    def askFruitsMango(self):
        while (True):
            try:
                print("망고를 추가하시겠습니까? 추가 : 'True' 거부 : 'False'\n")
                self.addFruitsMango = str(input())
                if self.addFruitsMango == 'True':
                    self.addList.append("addFruitsMango")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addFruitsMango = int(input())
                    self.addList.append(int(self.addFruitsMango))
                    self.__allPrice = self.__allPrice + (
                        int(self.addFruitsMango) * 1000)
                    break
                elif self.addFruitsMango == 'False':
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #def addFruitsStrawberry
    def askFruitsStrawberry(self):
        while (True):
            try:
                print("딸기를 추가하시겠습니까? 추가 : 'True' 거부 : 'False'\n")
                self.addFruitsStrawberry = str(input())
                if self.addFruitsStrawberry == 'True':
                    self.addList.append("addFruitsStrawberry")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addFruitsStrawberry = int(input())
                    self.addList.append(int(self.addFruitsStrawberry))
                    self.__allPrice = self.__allPrice + (
                        int(self.addFruitsStrawberry) * 1000)
                    break
                elif self.addFruitsStrawberry == 'False':
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #def addFruitsBlueberry
    def askFruitsBlueberry(self):
        while (True):
            try:
                print("블루베리를 추가하시겠습니까? 추가 : 'True' 거부 : 'False'\n")
                self.addFruitsBlueberry = str(input())
                if self.addFruitsBlueberry == 'True':
                    self.addList.append("addFruitsBlueberry")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addFruitsBlueberry = int(input())
                    self.addList.append(int(self.addFruitsBlueberry))
                    self.__allPrice = self.__allPrice + (
                        int(self.addFruitsBlueberry) * 1000)
                    break
                elif self.addFruitsBlueberry == 'False':
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #def addIceCream iceWaffle
    def askIceCream(self):
        while (True):
            try:
                print("아이스크림을 추가하시겠습니까? 추가 : 'True' 거부 : 'False'\n")
                self.addIceCream = str(input())
                if self.addIceCream == 'True':
                    self.addList.append("addIceCream")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addIceCream = int(input())
                    self.addList.append(int(self.addIceCream))
                    self.__allPrice = self.__allPrice + (
                        int(self.addIceCream) * 500)
                    break
                elif self.addIceCream == 'False':
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #def addRedVelvetPowder
    def askRedVelvetPowder(self):
        while (True):
            try:
                print("레드벨벳 파우더를 추가하시겠습니까? 추가 : 'True' 거부 : 'False'\n")
                self.addRedVelvetPowder = str(input())
                if self.addRedVelvetPowder == 'True':
                    self.addList.append("addRedVelvetPowder")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addRedVelvetPowder = int(input())
                    self.addList.append(int(self.addRedVelvetPowder))
                    self.__allPrice = self.__allPrice + (
                        int(self.addRedVelvetPowder) * 500)
                    break
                elif self.addRedVelvetPowder == 'False':
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    #def addChocolatePowder
    def askChocolatePowder(self):
        while (True):
            try:
                print("초콜릿 파우더를 추가하시겠습니까? 추가 : 'True' 거부 : 'False'\n")
                self.addChocolatePowder = str(input())
                if self.addChocolatePowder == 'True':
                    self.addList.append("addChocolatePowder")
                    print("얼만큼 추가하시겠습니까? ")
                    self.addChocolatePowder = input()
                    self.addList.append(int(self.addChocolatePowder))
                    self.__allPrice = self.__allPrice + int(
                        self.addChocolatePowder)
                    break
                elif self.addChocolatePowder == 'False':
                    pass
                    break
                else:
                    raise Exception("올바르게 입력하세요")
                    continue
            except Exception:
                print("올바르게 입력하세요")
                continue
            return self.addList

    def getAllPrice(self):  #paymentManager에게 줄 allPrice(총 가격) getter
        return self.__allPrice

    #최종적으로 넘겨줄 리스트 orderList에 의한 getter
    def getOrderList(self) -> list:
        return self.orderlist

    def getAddList(self) -> list:
        return self.addList

    def addIngredient(self) -> list:
        # 각각의 메뉴에 추가될 재료들을 results 리스트에 추가해줌
        for i in range(len(self.orderlist)):
            if 'addShot' in self.orderlist[i]:
                self.results.append('샷 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'subShot' in self.orderlist[i]:
                self.results.append('샷 ' + self.orderlist[i + 1] + '개 빼기 ')
            elif 'addLemon' in self.orderlist[i]:
                self.results.append('레몬 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addStrawberry' in self.orderlist[i]:
                self.results.append('딸기 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addOrange' in self.orderlist[i]:
                self.results.append('오렌지 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addGreenTea' in self.orderlist[i]:
                self.results.append('그린티 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addCondensedMilk' in self.orderlist[i]:
                self.results.append('연유 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addVanillaSyrup' in self.orderlist[i]:
                self.results.append('바닐라 시럽 ' + self.orderlist[i + 1] +
                                    '개 추가 ')
            elif 'addCafeMocha' in self.orderlist[i]:
                self.results.append('모카 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addCinnamon' in self.orderlist[i]:
                self.results.append('시나몬 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addCaramelSyrup' in self.orderlist[i]:
                self.results.append('카라멜 시럽 ' + self.orderlist[i + 1] +
                                    '개 추가 ')
            elif 'addYogurt' in self.orderlist[i]:
                self.results.append('요거트 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addBerry' in self.orderlist[i]:
                self.results.append('베리 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addPineapple' in self.orderlist[i]:
                self.results.append('파인애플 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addChamomileTea' in self.orderlist[i]:
                self.results.append('카모마일 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addHibiscusTea' in self.orderlist[i]:
                self.results.append('히비스커스 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addPeachPowder' in self.orderlist[i]:
                self.results.append('복숭아 파우더 ' + self.orderlist[i + 1] +
                                    '개 추가 ')
            elif 'addLavenderTea' in self.orderlist[i]:
                self.results.append('라벤더 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addBlackTea' in self.orderlist[i]:
                self.results.append('블랙티 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addRoyalHoney' in self.orderlist[i]:
                self.results.append('꿀 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addMatcha' in self.orderlist[i]:
                self.results.append('말차 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addPeppermintTea' in self.orderlist[i]:
                self.results.append('페퍼민트 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addRooibosTea' in self.orderlist[i]:
                self.results.append('루이보스 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addWaffle' in self.orderlist[i]:
                self.results.append('와플 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addFruitsMango' in self.orderlist[i]:
                self.results.append('망고 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addFruitsStrawberry' in self.orderlist[i]:
                self.results.append('딸기 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addFruitsBlueberry' in self.orderlist[i]:
                self.results.append('블루베리 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addIceCream' in self.orderlist[i]:
                self.results.append('아이스크림 ' + self.orderlist[i + 1] + '개 추가 ')
            elif 'addRedVelvetPowder' in self.orderlist[i]:
                self.results.append('레드벨벳 파우더 ' + self.orderlist[i + 1] +
                                    '개 추가 ')
            elif 'addChocolatePowder' in self.orderlist[i]:
                self.results.append('초콜릿 파우더 ' + self.orderlist[i + 1] +
                                    '개 추가 ')

    def Character(self):
        for j in range(len(self.orderlist)):
            try:
                if self.orderlist[j] in self.menulist:
                    if self.orderlist[j + 2] == 'ICE':
                        self.results.append('ICE ' + self.orderlist[j] + ' ' +
                                            self.orderlist[j + 1] + '개')
                    elif self.orderlist[j + 2] == 'HOT':
                        self.results.append('HOT ' + self.orderlist[j] + ' ' +
                                            self.orderlist[j + 1] + '개')
                    else:
                        self.results.append(self.orderlist[j] + ' ' +
                                            self.orderlist[j + 1] + '개')
            except IndexError:
                self.results.append(self.orderlist[j] + ' ' +
                                    self.orderlist[j + 1] + '개')
            # 좋은 방법은 아닌 것 같지만 ice, hot이 정의된 메뉴일 경우에는
            # 메뉴 앞에 ice, hot을 붙여 줌

            if 'size' in self.orderlist[j]:
                self.results.append(self.orderlist[j + 1])
            # size를 append 해줌.

    def LoadName(self):
        self.orderlist = list(itertools.chain(*self.orderlist))
        self.orderlist = list(map(str, self.orderlist))
        for k in range(len(MenuPrinter().getMenu())):
            self.menulist.append(MenuPrinter().getMenu()[k].getName())
        # 메뉴 각각의 이름들을 menulist에 append 해줌

    def Print2(self):
        self.LoadName()
        self.Character()
        self.addIngredient()
        print('\n\n\n주문하신 메뉴가 맞는지 확인해 주십시오.')
        for l in range(len(self.results)):
            print('-' * 30)
            print(self.results[l])
        print('-' * 30)
        # 추가된 메뉴들을 최종적으로 출력해 줌
