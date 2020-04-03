# _*_ encoding: utf-8 _*_
from com.kakao.cafe.module.orderTaker import OrderTaker
from com.kakao.cafe.module.cafeWorker import CafeWorker
from com.kakao.cafe.module.menuPrinter import MenuPrinter
import itertools
'''
1. orderlist를 ordertaker로부터 받아온다.
2. 받아온 orderlist를 출력한다.
3. 사용자 입력을 받는다
'''


class OrderChecker(CafeWorker):
    def __init__(self):
        self.__userinput = ''
        # 출력할 최종 리스트를 정의해 줌

    def askOrderList(self) -> bool:
        # 사용자 입력을 받아서 yes면 True를 return, no면 False를 return해서
        # 메인 모듈에서 paymentManager로 넘어갈 지, orderTaker로 돌아갈 지 판단하게 함
        while (True):
            try:
                # 예외 처리를 통해 yes, no가 아닐 경우에는 다시 입력하게 함
                self.__userinput = input(
                    '\n맞으면 Y or YES, 틀리면 N or NO\n').lower()
                if self.__userinput == 'y' or self.__userinput == 'yes':
                    return True
                    break
                    # paymentManager로 넘어감.
                elif self.__userinput == 'n' or self.__userinput == 'no':
                    print('다시 주문해 주시기 바랍니다.\n\n\n')
                    return False
                    break
                    # orderTaker로 돌아가야 함.
                else:
                    raise Exception("Error")
            except Exception:
                print('올바르게 입력하세요.')

    def Print(self):
        print("-" * 30)
