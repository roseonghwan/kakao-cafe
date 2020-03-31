from com.kakao.cafe.module.cafeWorker import CafeWorker
from com.kakao.cafe.module.menuPrinter import MenuPrinter
from com.kakao.cafe.module.orderTaker import OrderTaker
from com.kakao.cafe.module.orderChecker import OrderChecker
from com.kakao.cafe.module.paymentManager import PaymentManager
from com.kakao.cafe.module.receiptPrinter import ReceiptPrinter


def main():
    menuPrinter = MenuPrinter()
    orderTaker = OrderTaker()
    orderChecker = OrderChecker()

    menuPrinter.Print()
    menuList = list()
    menuList = input().split()
    menuList = list(map(int, menuList))
    orderTaker.takeOrder(menuList)
    orderlist = orderTaker.getOrderList()
    orderChecker.LoadName()
    orderChecker.Character()
    orderChecker.addIngredient()
    print(orderTaker.getOrderList())
    orderChecker.Print()
    orderChecker.askOrderList()


if __name__ == '__main__':
    main()
