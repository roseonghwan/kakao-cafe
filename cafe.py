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
    paymentManager = PaymentManager()
    receiptPrinter = ReceiptPrinter()

    while True:
        menuPrinter.Print()
        orderTaker.Print()
        menuList = list()
        menuList = input().split()
        menuList = list(map(int, menuList))
        orderTaker.takeOrder(menuList)
        orderTaker.Print2()

        if orderChecker.askOrderList() == True:
            paymentManager.setCardBalance(10000)
            paymentManager.setCash(10000)
            paymentManager.selectPaymentWay(orderTaker.getAllPrice())

            receiptPrinter.Print(orderTaker.getOrderList(),
                                 orderTaker.getAllPrice(),
                                 paymentManager.getPaymentSystem(),
                                 paymentManager.getCash())
            break

        else:
            continue


if __name__ == '__main__':
    main()
