from com.kakao.cafe.module.cafeWorker import CafeWorker
from com.kakao.cafe.module.menuPrinter import MenuPrinter
from com.kakao.cafe.module.orderTaker import OrderTaker
from com.kakao.cafe.module.orderChecker import OrderChecker
from com.kakao.cafe.module.paymentManager import PaymentManager
from com.kakao.cafe.module.receiptPrinter import ReceiptPrinter
import itertools


def main():
    menuPrinter = MenuPrinter()
    orderTaker = OrderTaker()
    orderChecker = OrderChecker()

    while True:
        menuPrinter.Print()
        orderTaker.Print()
        menuList = list()
        menuList = input().split()
        menuList = list(map(int, menuList))
        orderTaker.takeOrder(menuList)
        orderTaker.Print2()
        if orderChecker.askOrderList() == True:
            break
        else:
            continue
    print("결제")


if __name__ == '__main__':
    main()
