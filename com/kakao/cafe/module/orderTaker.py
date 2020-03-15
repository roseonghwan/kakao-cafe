# 주문 안내 메세지 출력 및 주문받음
#-*- coding:utf-8 -*-
from __future__ import print_function, absolute_import
from com.kakao.cafe.module.menuPrinter import MenuPrinter  #MenuPrinter에 있는 menuList를 가져오기 위해서
from com.kakao.cafe.module.cafeWorker import CafeWorker
import time  #영수증 출력할 때 주문시간을 나오게 하기 위해서 5번
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

# 2020-03-12 오후 16시 기준
남아있는 해야할 과제
1. 주문시간.. 넘겨줄.. 싫다
'''


class OrderTaker(CafeWorker):
    def __init__(self):
        self.__orderList = list()  #멤버변수 orderList 최종적으로 넘겨줄 리스트
        self.__allPrice = int()  #총 가격을 더할 멤버 변수

    def Print(self) -> None:
        print("---------------주문 안내 메시지---------------")
        print("---메뉴 리스트에 나와있는 숫자를 입력해주세요---")

    def takeOrder(self, menuList):  #손님에게 주문을 받는 함수 takeOrder
        #메뉴리스트에 있는 숫자까지 입력해야되는 걸 구분해야됨.
        '''
        try:
            self.__ordertoCustomer = input().split(
            )  #문자열 리스트로 받는 input을 만들어준다.
            self.__ordertoCustomer = list(map(
                int,
                self.__ordertoCustomer))  #문자열 리스트를 정수형으로 바꿨을때 Error가 나면 안됨.
            for length in len(self.__ordertoCustomer):
                if self.__ordertoCustomer >= 1 and self.__ordertoCustomer <= 30:
                    #메뉴 숫자가 30까지이기때문에 그사이에 안들어가면 오류남.
                    pass
                else:  #에러를 일부러 내야하는데 고민좀 해봐야겠음.
                    1 / 0
        except Exception:  #모든 시스템 종료 외의 내장 예외는 이 클래스에 파생됨.
            print("메뉴리스트에 있는 숫자로 다시 입력해주시오")
        '''
        self.__allPrice = 0  #주문을 할 때 마다 총 가격을 0으로 초기화해준다.
        #손님이 주문한 번호와 같은지 판별헤서 같으면 메뉴에 관한 옵션을 출력함.
        for Length in range(len(menuList)):  #손님에게 주문받은 ordertoCustmore만큼 반복
            #손님이 주문한 번호를 간략하게 바꿔놓는다.
            number = menuList[Length]
            #에스프레소
            if number == 1:
                addName(number)  #orderlist에 getName추가
                askAmount()  #수량 확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askAddshot()  #샷 추가 확인
                askSizeUp()  #사이즈업 확인
                #에스프레소는 차갑게 먹을 수 없으므로 askIced 메소드를 물어볼 필요 없음
            #아메리카노 - 에스프레스 상속
            elif number == 2:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askAddshot()  #샷 추가 확인
                askSizeUp()  #사이즈업 확인
                askIced()  #Iced확인
            #라떼 - 에스프레스 상속
            elif number == 3:
                addName(number)
                askAmount()  #수량 확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askAddshot()  #샷 추가 확인
                askSizeUp()  #사이즈업 확인
                askIced()  #Iced 확인
            #그린티라떼 - 라떼 상속
            elif number == 4:
                addName(number)
                askAmount()  #수량 확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askAddshot()  #샷 추가 확인
                askSizeUp()  #사이즈업 확인
                askIced()  #Iced 확인
                askGreenTea()  #GreenTea 추가 확인
                askCondensedMilk()  #연유 추가 확인
            #바닐라라떼 - 라떼 상속
            elif number == 5:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askAddshot()  #샷 추가 확인
                askSizeUp()  #사이즈업 확인
                askIced()  # Iced 확인
                askVanillaSyrup()  #바닐라 시업 추가 확인
            #카페모카 - 라떼 상속
            elif number == 6:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askAddshot()  #샷 추가 확인
                askSizeUp()  #사이즈업 확인
                askIced()  # Iced 확인
                askCafeMocha()  #모카 추가 확인
            #카푸치노 - 라떼 상속
            elif number == 7:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askAddshot()  #샷 추가 확인
                askSizeUp()  #사이즈업 확인
                askIced()  # Iced 확인
                askCinnamon()  #시나몬 추가 확인
            #카라멜마끼야또 - 라떼 상속
            elif number == 8:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askAddshot()  #샷 추가 확인
                askSizeUp()  #사이즈업 확인
                askIced()  # Iced 확인
                askCaramelSyrup()  #카라멜시럽 추가 확인
            #레몬에이드
            elif number == 9:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                #askIced()  # 뜨겁게 못하시때문에 물어보지않는다.
                askLemon()  # 레몬 추가 확인
            #오렌지에이드
            elif number == 10:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                #askIced()  # 뜨겁게 못하시때문에 물어보지않는다.
                askOrange()  # 오렌지 추가 확인
            #딸기에이드
            elif number == 11:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                #askIced()  # 뜨겁게 못하시때문에 물어보지않는다.
                askStrawberry()  # 딸기 추가 확인
            #요거트스무디
            elif number == 12:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askYogurt()  #요거트 추가 확인
            #블루베리스무디
            elif number == 13:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askBerry()  #블루베리 추가 확인
            #파인애플스무디
            elif number == 14:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askPineapple()  #파인애플 추가 확인
            #카모마일 차
            elif number == 15:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askChamomileTea()  #카모마일 추가 확인
            #그린티
            elif number == 16:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askGreenTea()  #그린티추가 그린티 라떼도 있으므로 getPrice가 다를 시 분류해줘야함.
            #히비스커스 티
            elif number == 17:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askHibiscusTea()  #카모마일 추가 확인
            #아이스티
            elif number == 18:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askPeachPowder()  #복숭아 파우더 추가 확인
            #라벤더 티
            elif number == 19:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askLavenderTea()  #라벤더 추가 확인
            #로얄밀크 티
            elif number == 20:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askBlackTea()  #블랙티 추가 확인
                askRoyalHoney()  #꿀 추가 확인
            #맛차 밀크 티
            elif number == 21:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askBlackTea()  #블랙티 추가 확인
                askCondensedMilk()  #연유 추가 확인
            #페퍼민트 티
            elif number == 22:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askPeppermintTea()  #페퍼민트 티 추가 확인
            #루이보스 티
            elif number == 23:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askRooibosTea()  #루이보스 티 추가 확인
            #벨기안 와플
            elif number == 24:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askWaffle()  #와플 추가
            #과일 와플
            elif number == 25:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askWaffle()  #와플 추가
                askFruitsMango()  #망고 추가 확인
                askFruitsStrawberry()  #딸기 추가 확인
                askFruitsBlueberry()  # 블루베리 추가 확인
            #아이스크림 와플
            elif number == 26:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askWaffle()  #와플 추가
                askIceCream()  #아이스크림 추가
            #뉴욕치즈케이크~
            elif number == 27:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
            #무지개치즈케이크
            elif number == 28:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
            #레드벨벳치즈케이크
            elif number == 29:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askRedVelvetPowder()  #레드벨벳 파우더 추가 확인
            #티라미수 케이크
            elif number == 30:
                addName(number)
                askAmount()  #수량확인
                addallPrice(number)  # 총 가격을 구하기위해 수량을 넣어줌
                askChocolatePowder()  #초콜릿 파우더 확인
            else:
                print(" E R R O R ")

    #orderList에 메뉴를 추가하는 매소드
    #Menu는 MenuPrinter에 있는 객체들을 나누기 위해서 사용함. 손님에게 받은 수
    #중간중간 Menu를 따로 빼주는 거는 메뉴마다 리스트가 서로 달리 존재하기 때문에
    #그 전의 리스트 Length만큼 빼주는 것이다.
    #<완료>
    def addName(self, Menu: int) -> list:
        if Menu <= 8:  # 1~8 에스프레스
            self.__orderList.append(MenuPrinter.getEspresso()[Menu].getName())
        elif Menu <= 11:
            Menu -= 9  # 9~11 에이드
            self.__orderList.append(MenuPrinter.getAde()[Menu].getName())
        elif Menu <= 14:
            Menu -= 12  # 12~14 스무디
            self.__orderList.append(MenuPrinter.getSmoothie()[Menu].getName())
        elif Menu <= 23:
            Menu -= 15  # 15~ 23 티
            self.__orderList.append(MenuPrinter.getTea()[Menu].getName())
        else:
            Menu -= 24  # 24 ~ 30 디저트
            self.__orderList.append(MenuPrinter.getDessert()[Menu].getName())
        #return으로 self.__orderList를 해줌.
        return self.__orderList

    #수량을 질문하는 메소드
    #손님에게 묻는 수량이 int(정수형이 아니면) 에러나게 해야함.
    #<완료>
    def askAmount(self) -> list:
        try:
            print("수량을 입력해주세요 : ")
            amount = int(input())
            self.__orderList.append(amount)  #리스트에 수량을 추가함. 메뉴 다음에 있으면 편함.
        except Exception:
            print("수량을 다시 입력해주세요 ")
        return self.__orderList

    def addallPrice(self, price: int) -> list:
        if price <= 8:  # 1~8 에스프레스
            self.__allPrice = self.__allPrice + (
                MenuPrinter.getEspresso()[price].getPrice() *
                self.__orderList[len - 1])
        elif price <= 11:
            price -= 9  # 9~11 에이드
            self.__allPrice = self.__allPrice + (
                MenuPrinter.getAde()[price].getPrice() *
                self.__orderList[len - 1])
        elif price <= 14:
            price -= 12  # 12~14 스무디
            self.__allPrice = self.__allPrice + (
                MenuPrinter.getSmoothie()[price].getPrice() *
                self.__orderList[len - 1])
        elif price <= 23:
            price -= 15  # 15~ 23 티
            self.__allPrice = self.__allPrice + (
                MenuPrinter.getTea()[price].getPrice() *
                self.__orderList[len - 1])
        else:
            price -= 24  #23 ~ 30 디저트
            self.__allPrice = self.__allPrice + (
                MenuPrinter.getDessert()[price].getPrice() *
                self.__orderList[len - 1])
        return self.__allPrice

    #------------------------------Add Options--------------------------
    #샷을 질문하는 메소드
    #<완료>
    def askAddshot(self) -> float:
        try:
            print("삿을 추가하시거나 빼시겠습니까? 추가하거나 빼면 : True 기본 : False")
            self.askShot = input()
            #샷을 추가하거나 빼면 어떻게 할지 물어본다.
            if self.askShot == True:
                print("샷 추가 : True 샷 빼기 : False")
                self.Shot = input()
                if self.Shot == True:  #샷 추가
                    self.__orderList.append('addShot')
                    print("샷 추가를 얼마나 하시겠습니까? ")
                    self.addShot = int(input())
                    self.__orderList.append(float(self.addShot))
                    self.__allPrice = self.__allPrice + (int(
                        self.addShot * 500))
                elif self.Shot == False:
                    self.__orderList.append('subShot')
                    print("샷을 얼마나 빼시겠습니까? ")
                    self.subShot = int(input())
                    self.__orderList.append(float(self.subShot))
                    self.__allPrice = self.__allPrice - (int(
                        self.subShot * 500))
                else:
                    raise Exception("다시 입력해주시기 바랍니다")
            #샷을 기본으로 하면 pass한다.
            elif self.askShot == False:
                pass
            else:
                raise Exception("다시 입력해주시기 바랍니다")
        except Exception:
            print("다시 입력해주시기 바랍니다.")

    #hot or ice를 물어보는 메소드
    def askIced(self) -> bool:
        try:
            print("ICE는 True HOT는 False로 입력해주십시오 ")
            self.ice = input()
            if self.ice == True:
                self.__orderList.append('ICE')
            elif self.ice == False:
                self.__orderList.append('HOT')
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주십시오")

    #사이즈 추가 Espresson method
    def askSizeUp(self) -> str:
        try:
            print("사이즈를 추가하시겠습니까? 추가 : True 기본 : False")
            self.sizeup = input()
            if self.sizeup == True:
                self.__orderList.append("sizeUp")
                print("Grande : True , Venti : False")
                self.Choose = int(input())
                if self.Choose == True:
                    self.__orderList.append('Grande')
                    self.__allPrice = self.__allPrice + 500
                elif self.Choose == False:
                    self.__orderList.append('Venti')
                    self.__allPrice = self.__allPrice + 500
                else:
                    raise Exception("다시 입력해주십시오")
            elif self.sizeup == False:
                pass
            else:
                raise Exception("다시 입력해주십시오")
        except Exception:
            print("다시 입력해주십시오")

    #GreenTea add Option 16 GreenTea
    def askGreenTea(self):
        try:
            print("그린티를 추가하시겠습니까? 추가 : True 기본 : False")
            self.addGreenTea = input()
            if self.addGreenTea == True:
                self.__orderList.append("addGreanTea")
                print("얼만큼 추가하시겠습니까? ")
                self.addGreenTea = int(input())
                self.__orderList.append(int(self.addGreenTea))
                self.__allPrice = self.__allPrice + (int(self.addGreenTea) *
                                                     300)
            elif self.addGreenTea == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주십시오")

    #GreenTea condenseMilk Option
    def askCondensedMilk(self):
        try:
            print("연유 추가하시겠습니까? 추가 : True 기본 : False")
            self.addMilk = input()
            if self.addMilk == True:
                self.__orderList.append("addCondensedMilk")
                print("얼만큼 추가하시겠습니까? ")
                self.addMilk = int(input())
                self.__orderList.append(int(self.addMilk))
                self.__allPrice = self.__allPrice + (int(self.addMilk) * 300)
            elif self.addMilk == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #VanillaLatte Option
    def askVanillaSyrup(self):
        try:
            print("바닐라 시럽 추가하시겠습니까? 추가 : True 기본 : False")
            self.addSyrup = input()
            if self.addSyrup == True:
                self.__orderList.append('addVanillaSyrup')
                print("얼만큼 추가하시겠습니까? ")
                self.addSyrup = int(input())
                self.__orderList.append(int(self.addSyrup))
                self.__allPrice = self.__allPrice + (int(self.addSyrup) * 200)
            elif self.addSyrup == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #CafeMocha 카페모카 추가 옵션
    def askCafeMocha(self):
        try:
            print("모카 추가하시겠습니까? 추가 : True 기본 : False")
            self.addMocha = input()
            if self.addMocha == True:
                self.__orderList.append('addCafeMocha')
                print("얼만큼 추가하시겠습니까? ")
                self.addMocha = int(input())
                self.__orderList.append(int(self.addMocha))
                self.__allPrice = self.__allPrice + (int(self.addMocha) * 300)
            elif self.addMocha == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #Cappuccino 카푸치노 추가 옵션
    def askCinnamon(self):
        try:
            print("시나몬 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addCinnamon = input()
            if self.addCinnamon == True:
                self.__orderList.append('addCinnamon')
                print("얼만큼 추가하시겠습니까? ")
                self.addCinnamon = int(input())
                self.__orderList.append(int(self.addCinnamon))
                self.__allPrice = self.__allPrice + self.addCinnamon  #약간 이상한느낌이 들음....  + amount?
            elif self.addCinnamon == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #CaramelMacchiato
    def askCaramelSyrup(self):
        try:
            print("카라멜 시럽 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addSyrup = input()
            if self.addSyrup == True:
                self.__orderList.append('addCaramelSyrup')
                print("얼만큼 추가하시겠습니까? ")
                self.addSyrup = int(input())
                self.__orderList.append(int(self.addSyrup))
                self.__allPrice = self.__allPrice + (int(self.addSyrup) * 200)
            elif self.addSyrup == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #LemonAde 레몬에이드 레몬추가 addOption
    def askLemon(self):
        try:
            print("레몬 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addLemon = input()
            if self.addLemon == True:
                self.__orderList.append('addLemon')
                print("얼만큼 추가하시겠습니까? ")
                self.addLemon = int(input())
                self.__orderList.append(int(self.addLemon))
                self.__allPrice = self.__allPrice + (int(self.addLemon) * 500)
            elif self.addLemon == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    def askOrange(self):
        try:
            print("오렌지 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addOrange = input()
            if self.addOrange == True:
                self.__orderList.append('addOrange')
                print("얼만큼 추가하시겠습니까? ")
                self.addOrange = int(input())
                self.__orderList.append(int(self.addOrange))
                self.__allPrice = self.__allPrice + (int(self.addOrange) * 500)
            elif self.addOrange == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #StrawberryAde 딸기 추가
    def askStrawberry(self):
        try:
            print("딸기 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addStrawberry = input()
            if self.addStrawberry == True:
                self.__orderList.append('addStrawberry')
                print("얼만큼 추가하시겠습니까? ")
                self.addStrawberry = int(input())
                self.__orderList.append(int(self.addStrawberry))
                self.__allPrice = self.__allPrice + (int(self.addStrawberry) *
                                                     500)
            elif self.addStrawberry == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #YogurtSmoothie 요거트 추가
    def askYogurt(self):
        try:
            print("요거트 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addYogurt = input()
            if self.addYogurt == True:
                self.__orderList.append('addYogurt')
                print("얼만큼 추가하시겠습니까? ")
                self.addYogurt = int(input())
                self.__orderList.append(int(self.addYogurt))
                self.__allPrice = self.__allPrice + (int(self.addYogurt) * 500)
            elif self.addYogurt == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #BerryBerrySmoothie 요거트 추가
    def askBerry(self):
        try:
            print("베리 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addBerry = input()
            if self.addBerry == True:
                self.__orderList.append('addBerry')
                print("얼만큼 추가하시겠습니까? ")
                self.addBerry = int(input())
                self.__orderList.append(int(self.addBerry))
                self.__allPrice = self.__allPrice + (int(self.addBerry) * 500)
            elif self.addBerry == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #PineappleSmoothie 파인애플 추가
    def askPineapple(self):
        try:
            print("파인애플 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addPineapple = input()
            if self.addPineapple == True:
                self.__orderList.append("addPineapple")
                print("얼만큼 추가하시겠습니까? ")
                self.addPineapple = int(input())
                self.__orderList.append(int(self.addPineapple))
                self.__allPrice = self.__allPrice + (int(self.addPineapple) *
                                                     500)
            elif self.addPineapple == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #ChamomileTea 카모마일 차
    def askChamomileTea(self):
        try:
            print("카모마일을 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addChamomileTea = input()
            if self.addChamomileTea == True:
                self.__orderList.append("addChamomileTea")
                print("얼만큼 추가하시겠습니까? ")
                self.addChamomileTea = int(input())
                self.__orderList.append(int(self.addChamomileTea))
                self.__allPrice = self.__allPrice + (
                    int(self.addChamomileTea) * 500)
            elif self.addChamomileTea == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #HibiscusTea 히비스커스 티?
    def askHibiscusTea(self):
        try:
            print("카모마일을 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addHibiscusTea = input()
            if self.addHibiscusTea == True:
                self.__orderList.append("addHibiscusTea")
                print("얼만큼 추가하시겠습니까? ")
                self.addHibiscusTea = int(input())
                self.__orderList.append(int(self.addHibiscusTea))
                self.__allPrice = self.__allPrice + (int(self.addHibiscusTea) *
                                                     500)
            elif self.addHibiscusTea == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #Icetea 피치파우더
    def askPeachPowder(self):
        try:
            print("복숭아 파우더를 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addPeachPowder = input()
            if self.addPeachPowder == True:
                self.__orderList.append("addPeachPowder")
                print("얼만큼 추가하시겠습니까? ")
                self.addPeachPowder = int(input())
                self.__orderList.append(int(self.addPeachPowder))
                self.__allPrice = self.__allPrice + (int(self.addPeachPowder) *
                                                     400)
            elif (self.addPeachPowder == False):
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #LavenderTea
    def askLavenderTea(self):
        try:
            print("라벤더를 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addLavenderTea = input()
            if self.addLavenderTea == True:
                self.__orderList.append("addLavenderTea")
                print("얼만큼 추가하시겠습니까? ")
                self.addLavenderTea = int(input())
                self.__orderList.append(int(self.addLavenderTea))
                self.__allPrice = self.__allPrice + (int(self.addLavenderTea) *
                                                     500)
            elif (self.addLavenderTea == False):
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #RoyalMilkTea BlackTea
    def askBlackTea(self) -> float:
        try:
            print("블랙티를 추가하시거나 빼시겠습니까? 추가하거나 빼면 : True 기본 : False")
            self.BlackTea = input()
            #블랙티을 추가하거나 빼면 어떻게 할지 물어본다.
            if self.BlackTea == True:
                print("블랙티 추가 : True 블랙티 빼기 : False")
                self.BlackTea = input()
                if (self.BlackTea == True):  #블랙티 추가
                    self.__orderList.append('addBlackTea')
                    print("블랙티 추가를 얼마나 하시겠습니까? ")
                    self.addBlackTea = int(input())
                    self.__orderList.append(float(self.addBlackTea))
                    self.__allPrice = self.__allPrice + (
                        int(self.addBlackTea) * 500)
                elif (self.BlackTea == False):
                    self.__orderList.append('subBlackTea')
                    print("블랙티을 얼마나 빼시겠습니까? ")
                    self.subBlackTea = int(input())
                    self.__orderList.append(float(self.subBlackTea))
                    self.__allPrice = self.__allPrice - int(self.subBlackTea)
                else:
                    raise Exception("다시 입력해주시기 바랍니다")
            #블랙티을 기본으로 하면 pass한다.
            elif self.askBlackTea == False:
                pass
            else:
                raise Exception("다시 입력해주시기 바랍니다")
        except Exception:
            print("다시 입력해주시기 바랍니다.")

    #royalMilkTea addRoyalHoney
    def askRoyalHoney(self):
        try:
            print("꿀을 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addRoyalHoney = input()
            if self.addRoyalHoney == True:
                self.__orderList.append("addRoyalHoney")
                print("얼만큼 추가하시겠습니까? ")
                self.addRoyalHoney = int(input())
                self.__orderList.append(int(self.addRoyalHoney))
                self.__allPrice = self.__allPrice + (int(self.addRoyalHoney) *
                                                     1000)
            elif self.addRoyalHoney == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #addMatcha matchaMilkTea
    def askMatcha(self):
        try:
            print("말차를 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addMatcha = input()
            if self.addMatcha == True:
                self.__orderList.append("addMatcha")
                print("얼만큼 추가하시겠습니까? ")
                self.addMatcha = int(input())
                self.__orderList.append(int(self.addMatcha))
                self.__allPrice = self.__allPrice + (int(self.addMatcha) * 400)
            elif self.addMatcha == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #addPeppermintTea  peppermintTea
    def askPeppermintTea(self):
        try:
            print("페퍼민트를 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addPeppermintTea = input()
            if self.addPeppermintTea == True:
                self.__orderList.append("addPeppermintTea")
                print("얼만큼 추가하시겠습니까? ")
                self.addPeppermintTea = int(input())
                self.__orderList.append(int(self.addPeppermintTea))
                self.__allPrice = self.__allPrice + (
                    int(self.addPeppermintTea) * 500)
            elif self.addPeppermintTea == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #addRooibosTea rooibosTea
    def askRooibosTea(self):
        try:
            print("루이보스를 추가하시겠습니까? 추가 : True 기본 : False\n")
            self.addRooibosTea = input()
            if self.addRooibosTea == True:
                self.__orderList.append("addRooibosTea")
                print("얼만큼 추가하시겠습니까? ")
                self.addRooibosTea = int(input())
                self.__orderList.append(int(self.addRooibosTea))
                self.__allPrice = self.__allPrice + (int(self.addRooibosTea) *
                                                     700)
            elif self.addRooibosTea == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #def addWaffle beiganWaffle FruitsWaffle
    def askWaffle(self):
        try:
            print("와플을 추가하시겠습니까? 추가 : True 거부 : False\n")
            self.addWaffle = input()
            if self.addWaffle == True:
                self.__orderList.append("addWaffle")
                print("얼만큼 추가하시겠습니까? ")
                self.addWaffle = int(input())
                self.__orderList.append(int(self.addWaffle))
                self.__allPrice = self.__allPrice + (int(self.addWaffle) *
                                                     1000)
            elif self.addWaffle == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #def addFruitsMango
    def askFruitsMango(self):
        try:
            print("망고를 추가하시겠습니까? 추가 : True 거부 : False\n")
            self.addFruitsMango = input()
            if self.addFruitsMango == True:
                self.__orderList.append("addFruitsMango")
                print("얼만큼 추가하시겠습니까? ")
                self.addFruitsMango = int(input())
                self.__orderList.append(int(self.addFruitsMango))
                self.__allPrice = self.__allPrice + (int(self.addFruitsMango) *
                                                     1000)
            elif self.addFruitsMango == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #def addFruitsStrawberry
    def askFruitsStrawberry(self):
        try:
            print("딸기를 추가하시겠습니까? 추가 : True 거부 : False\n")
            self.addFruitsStrawberry = input()
            if self.addFruitsStrawberry == True:
                self.__orderList.append("addFruitsStrawberry")
                print("얼만큼 추가하시겠습니까? ")
                self.addFruitsStrawberry = int(input())
                self.__orderList.append(int(self.addFruitsStrawberry))
                self.__allPrice = self.__allPrice + (
                    int(self.addFruitsStrawberry) * 1000)
            elif self.addFruitsStrawberry == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #def addFruitsBlueberry
    def askFruitsBlueberry(self):
        try:
            print("블루베리를 추가하시겠습니까? 추가 : True 거부 : False\n")
            self.addFruitsBlueberry = input()
            if self.addFruitsBlueberry == True:
                self.__orderList.append("addFruitsBlueberry")
                print("얼만큼 추가하시겠습니까? ")
                self.addFruitsBlueberry = int(input())
                self.__orderList.append(int(self.addFruitsBlueberry))
                self.__allPrice = self.__allPrice + (
                    int(self.addFruitsBlueberry) * 1000)
            elif self.addFruitsBlueberry == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #def addIceCream iceWaffle
    def askIceCream(self):
        try:
            print("아이스크림을 추가하시겠습니까? 추가 : True 거부 : False\n")
            self.addIceCream = input()
            if self.addIceCream == True:
                self.__orderList.append("addIceCream")
                print("얼만큼 추가하시겠습니까? ")
                self.addIceCream = int(input())
                self.__orderList.append(int(self.addIceCream))
                self.__allPrice = self.__allPrice + (int(self.addIceCream) *
                                                     500)
            elif self.addIceCream == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #def addRedVelvetPowder
    def askRedVelvetPowder(self):
        try:
            print("레드벨벳 파우더를 추가하시겠습니까? 추가 : True 거부 : False\n")
            self.addRedVelvetPowder = input()
            if self.addRedVelvetPowder == True:
                self.__orderList.append("addRedVelvetPowder")
                print("얼만큼 추가하시겠습니까? ")
                self.addRedVelvetPowder = int(input())
                self.__orderList.append(int(self.addRedVelvetPowder))
                self.__allPrice = self.__allPrice + (
                    int(self.addRedVelvetPowder) * 500)
            elif self.addRedVelvetPowder == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    #def addChocolatePowder
    def askChocolatePowder(self):
        try:
            print("초콜릿 파우더를 추가하시겠습니까? 추가 : True 거부 : False\n")
            self.addChocolatePowder = input()
            if self.addChocolatePowder == True:
                self.__orderList.append("addChocolatePowder")
                print("얼만큼 추가하시겠습니까? ")
                self.addChocolatePowder = input()
                self.__orderList.append(int(self.addChocolatePowder))
                self.__allPrice = self.__allPrice + int(
                    self.addChocolatePowder)
            elif self.addChocolatePowder == False:
                pass
            else:
                raise Exception("다시 입력해주세요")
        except Exception:
            print("다시 입력해주세요")

    def allPrice(self, amount):  #paymentManager에게 줄 allPrice(총 가격) getter
        return self.__allPrice

    #최종적으로 넘겨줄 리스트 orderList에 의한 getter
    def getOrderList(self) -> list:
        return self.__orderList
