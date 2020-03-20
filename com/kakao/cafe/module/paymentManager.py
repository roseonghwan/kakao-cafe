#-*- coding:utf-8 -*-
from com.kakao.cafe.module.orderTaker import OrderTaker


class PaymentManager:
    def __init__(self):
        self.totalPrice = OrderTaker().getAllPrice(
        )  # OrderTaker클래스에서 getAllPrice 함수를 가져오기 위해 OrderTaker클래스의 객체 생성
        self.__paymentSystem = ''  #결제 수단
        self.__cardBalance = 0  #카드 잔액
        self.__cash = 0  #소유 현금
        self.__change = 0  #거스름돈
        self.__point = 0  #적립 포인트

    def selectPaymentWay(self):  # 결제수단을 고르는 함수
        select_example = {  #결제  보기
            1: "카드",
            2: "현금",
        }  # key가 번호이고 value가 결제수단인 딕셔너리
        try:
            print("\n1. 카드 \n2. 현금")  # 보기 출력
            select = int(input("결제방법을 선택하세요. \t"))  # 사용자가 key값인 번호로 선택
            self.__paymentSystem = select_example[
                select]  # 사용자가 key값인 번호를 누르면 결제수단인 value가 paymentSystem에 입력되도록 함
            print(self.getPaymentSystem() + "(으)로 결제를 진행하겠습니다.")
            if self.getPaymentSystem() == "카드":  # 카드결제로 진행
                return self.cardPay()
            elif self.getPaymentSystem() == "현금":  # 현금결제로 진행
                return self.cashPay()
        except ValueError:  # 입력한 수가 숫자가 아닌 경우
            print("보기를 보고 다시 입력하세요.")
        except KeyError:  # 입력한 숫자가 select_example의 key값들이 아닌 경우
            print("보기를 보고 다시 입력하세요.")

    def cardPay(self):  # 카드결제
        select_example = {1: "예", 2: "아니요"}  # 포인트를 사용할지 여부
        if self.__cardBalance >= self.totalPrice:
            try:
                select = int(input("포인트를 사용하시겠습니까?\t"))
                print("\n1. 예\n2. 아니오")
                if select == 1:  # 포인트를 사용해 할인되어 결제하는 경우
                    self.totalPrice -= self.getPoint()
                    self.__cardBalance -= self.totalPrice
                    print("포인트 사용 후 카드결제가 완료되었습니다.")
                    self.__point = 0  # 포인트를 사용한 후 포인트는 0으로 됨
                else:  # 포인트를 사용하지 않고 결제하는 경우
                    self.__cardBalance -= self.totalPrice
                    print("카드결제가 완료되었습니다.")
                    self.__point = self.__point + self.totalPrice * 0.03  # 포인트를 사용하지 않고 결제한 경우 가격의 3%가 적립되어 point에 저장됨
                    print("적립된 포인트는 " + str(self.getPoint()) + "원 입니다.")
            except ValueError:  # 입력한 수가 숫자가 아닌 경우
                print("보기를 보고 다시 입력하세요.")
            except KeyError:  # 입력한 숫자가 select_example의 key값들이 아닌 경우
                print("보기를 보고 다시 입력하세요.")
        else:
            print("잔액이 부족합니다.")
        return self.__point

    def cashPay(self):  # 현금결제
        if self.__cash >= self.totalPrice:
            self.__change = self.__cash - self.totalPrice  # 거스름돈 계산
            print("받은금액은 " + str(self.getCash()) + "원 입니다.")
            print("거스름돈은 " + str(self.getChange()) + "원 입니다.")
            print("현금결제가 완료되었습니다.")
        else:
            print("현금이 부족합니다.")

    def setCardBalance(
        self, cardBalance: int):  # 처음 카드잔액을 얼마로 설정할지 필요한 cardBalance의 setter
        self.__cardBalance = cardBalance

    def setCash(self, cash: int):  # 처음 현금을 얼마로 설정할지 필요한 cash의 setter
        self.__cash = cash

    def setTtotalPrice(
        self, totalPrice: int):  # 총 가격을 얼마로 설정할지 필요한 totalPrice의 setter
        self.totalPrice = totalPrice

    def setPoint(self, point: float):  # 처음 포인트를 얼마로 설정할지 필요한 point의 setter
        self.__point = point

    def getPaymentSystem(self):  # 어떤 수단으로 결제할지 나오는 paymentSystem의 getter
        return self.__paymentSystem

    def getCash(self):  # 현금 계산 시 낸 돈이 나오는 cash의 getter
        return self.__cash

    def getChange(self):  # 현금 계산할 시 거스름돈이 나오는 change의 getter
        return self.__change

    def getPoint(self):  # 카드 계산할 시 포인트가 나오는 poing의 getter
        return self.__point

    def getTotalPrice(self):
        return self.totalPrice