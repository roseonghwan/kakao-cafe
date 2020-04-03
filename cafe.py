
# -*- coding: utf-8 -*-
#
# cafe.py
#
# Main module of Kakao cafe.
#
# Copyright (c) 2020 Jonna Family
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

        if orderChecker.askOrderList() == 'True':
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
