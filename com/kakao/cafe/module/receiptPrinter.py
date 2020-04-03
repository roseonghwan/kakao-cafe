#-*- coding:utf-8 -*-
from com.kakao.cafe.module.cafeWorker import CafeWorker
from com.kakao.cafe.module.orderTaker import OrderTaker
from com.kakao.cafe.module.menuPrinter import MenuPrinter
from com.kakao.cafe.module.paymentManager import PaymentManager
from datetime import datetime


class ReceiptPrinter(CafeWorker):
    def __init__(self):

        # OrderTaker에 있는 orderlist를 가져옴
        self.namelist = list()  # 메뉴이름 가져오는 리스트 생성

    def Print(self, receiptList, allprice, paymentway, givenmoney) -> None:

        # 기본 틀
        print("\n")
        print("-" * 71)
        print(" " * 28 + "[  영수증  ]")
        print("-" * 71)

        print("[매장명]   카카오 카페")
        print("[주  소]   서울특별시 마포구 동교동 176-9")
        print("[대표자]   맹산하 외 5인")

        # 현재 시간 영수증에 표시
        print("[매출일]   " + datetime.today().strftime("%Y-%m-%d   %H:%M:%S"))

        # 기본 틀
        print("-" * 71)
        print("-" * 71)

        print("%20s%34s" % ("[상 품 명]", "[수 량]"))

        print("-" * 71)

        # 영수증 상품명, 단가, 수량, 가격 표시

        for k in range(len(
                MenuPrinter().getMenu())):  # 모든 메뉴의 이름을 namelist에 받아옴
            self.namelist.append(MenuPrinter().getMenu()[k].getName())

        for i in range(
                len(receiptList)
        ):  # r eceiptList 예시 : ['Espresso', '2', "ICE","addShot", 2, 'newYorkCheeseCake']
            if receiptList[
                    i] in self.namelist:  # 주문 메뉴 이름의 메뉴명, 수량과 핫/아이스 상태를 출력함
                self.name = receiptList[i]
                self.amount = receiptList[i + 1]
                try:

                    if (receiptList[i + 2] == "ICE"
                            or receiptList[i + 2] == "HOT"
                        ):  # 디저트는 "HOT","ICE"가 아니므로 제품명만 출력 구분
                        self.hot_ice = receiptList[i + 2]
                        print("%-25s%15s%16s" %
                              (self.name + "(" + self.hot_ice + ")", "|",
                               self.amount))
                    else:
                        print("%-25s%15s%16s" % (self.name, "|", self.amount))
                except IndexError:
                    print("%-25s%15s%16s" % (self.name, "|", self.amount))

        print("-" * 71)

        print("-" * 71)

        print("%-60s" % ("[결제수단] : " + paymentway))
        if paymentway == "카드":
            print("%-63s" % ("[받은  돈] : " + str(allprice) + "원"))
            print("%-63s" % ("[거스름돈] : " + str(allprice) + "원"))
        elif paymentway == "현금":
            print("%-63s" % ("[받은  돈] : " + str(givenmoney) + "원"))
            print("%-63s" % ("[거스름돈] : " + str(givenmoney - allprice) + "원"))

        print("-" * 71)

        print("%60s" % ("총 가격 : " + str(allprice) + "원"))


""" 출력 예시 ///

-----------------------------------------------------------------------
                            [  영수증  ]
-----------------------------------------------------------------------
[매장명]   카카오 카페
[주  소]   서울특별시 마포구 동교동 176-9
[대표자]   맹산하 외 5인
[매출일]   2020-03-20   17:45:51
-----------------------------------------------------------------------
-----------------------------------------------------------------------
             [상 품 명]                             [수 량]
-----------------------------------------------------------------------
BerryBerrySmoothie(ICE)                |               2
Espresso(ICE)                          |               2
-----------------------------------------------------------------------
[결제수단] : 현금                                                 
[받은  돈] : 20000원                                               
[거스름돈] : 10000원                                                
-----------------------------------------------------------------------
                                               총 가격 : 10000원

"""
