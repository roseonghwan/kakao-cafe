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
        self.menulist = list()
        self.orderlist = OrderTaker().getOrderList()
        # menulist와 orderlist의 주문 내역을 비교하기 위해 menulist와 orderlist를 정의해줌
        self.orderlist = list(itertools.chain(*self.orderlist))
        # orderlist에 들어온 여러 중의 리스트들을 하나의 리스트로 만들어 줌
        self.orderlist = list(map(str, self.orderlist))
        # orderlist의 data들을 모두 str 형으로 바꿔 줌
        self.results = list()
        # 출력할 최종 리스트를 정의해 줌

    def addIngredient(self) -> list:
        # 각각의 메뉴에 추가될 재료들을 results 리스트에 추가해줌
        for i in range(len(self.orderlist)):
            print(self.orderlist[i])
            if 'addShot' in self.orderlist[i]:
                self.results.append('샷 ' + self.orderlist[i + 1] + '개 추가 ')
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
            print(self.orderlist[j])
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
        for k in range(len(MenuPrinter().getMenu())):
            self.menulist.append(MenuPrinter().getMenu()[k].getName())
        # 메뉴 각각의 이름들을 menulist에 append 해줌

    def Print(self):
        print('주문하신 메뉴가 맞는지 확인해 주십시오.')
        for l in range(len(self.results)):
            print('-' * 30)
            print(self.results[l])
        print('-' * 30)
        # 추가된 메뉴들을 최종적으로 출력해 줌

    def askOrderList(self) -> str:
        # 사용자 입력을 받아서 yes면 True를 return, no면 False를 return해서
        # 메인 모듈에서 paymentManager로 넘어갈 지, orderTaker로 돌아갈 지 판단하게 함
        try:
            # 예외 처리를 통해 yes, no가 아닐 경우에는 다시 입력하게 함
            self.__userinput = input('\n맞으면 Y or YES, 틀리면 N or NO\n').lower()
            if self.__userinput == 'y' or self.__userinput == 'yes':
                return True
                # paymentManager로 넘어감.
            elif self.__userinput == 'n' or self.__userinput == 'no':
                return False
                # orderTaker로 돌아가야 함.
            else:
                raise Exception("Error")
        except Exception:
            print('올바르게 입력하세요.')