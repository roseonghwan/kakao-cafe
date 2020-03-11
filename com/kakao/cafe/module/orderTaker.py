from com.kakao.cafe.module.menuPrinter import MenuPrinter #MenuPrinter에 있는 menuList를 가져오기 위해서

import time #영수증 출력할 때 주문시간을 나오게 하기 위해서 5번


'''
0. 중요한건 메인모듈에서 인스턴스화해서 내게 넣어주기 때문에
   내가 모든걸 import하거나 인스턴스화를 할 필요가 없다.
1. 손님에게 메뉴리스트에 있는 숫자만을 입력해달라고 한다.
2. MenuPrinter에서 받은 리스트와 손님에게 받은 숫자를 비교하여
3. 같으면 그 메뉴에 대한 수량을 묻고 추가 옵션에 대해서 나온다.(동시에 시간(선입선출하기 위해서)과 총 가격을 출력하기 위해서 Price까지 받는다.)
4. 손님이 선택한 항목을 OrderList에 차례대로 입력해준다.
5. 4번 항목인 paymentManager에게 allPrice(총가격)을 주기 위해서 함수를 제공한다.
6. OrderList는 5번 receiptPrinter에게 줄 품목, 수량을 주기위함, 함수를 편히 제공하기 위해 선언한다.
''' 
class OrderTaker(self):
    def __init__(self, menuList):
    
def takeOrder(self): #손님에게 주문을 받는 함수 takeOrder
    print("---------------주문 안내 메시지---------------")
    print("---메뉴 리스트에 나와있는 숫자를 입력해주세요---")
    try: #메뉴리스트에 있는 숫자까지 입력해야되는 걸 구분해야됨.
        self.__orderList = input().split() #문자열 리스트로 받는 input을 만들어준다.
    except ValueError:
        print("메뉴리스트에 있는 숫자로 다시 입력해주시오")
    
    for Length in range(self.__orderList):
        
        
        

    
def getAde(self):
    return True

def getEspresso(self, order):
    return True

def addList(self, amount):
    return True

def allPrice(self, amount): #paymentManager에게 줄 allPrice(총 가격) getter
    return True