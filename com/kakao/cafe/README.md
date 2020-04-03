# 카페 주문 시스템 구현

안녕하세요, 카카오 신입 크루 여러분.

경영본부의 귀여움을 담당하고 있는 라이언입니다.

카카오는 다가오는 봄을 맞아 '카카오 카페' 시스템을 구축하기로 했습니다.

'카카오 카페'는 카카오의 야심찬 신년 프로젝트로, 전국의 카페 매장들을 타겟으로 하는 대규모 결제 플랫폼 프로젝트의 일환입니다.

올해 6월까지 카카오 페이, 카카오 뱅크 등과 연동하여 카카오 플랫폼에 포함시켜 상용화할 예정이며, 예상 수익은 연 1200억원으로 추정하고 있습니다.

현재 개발 책임팀에서 최종 설계를 디자인 중이며, 신입 개발팀은 아래의 API 명세에 따라 코드를 구현해주시면 됩니다.

---

## 카카오 카페 결제 모듈 구현 명세

카카오 카페는 카페 메뉴 정보 제공과 결제 및 영수중 발행까지의 기능을 갖춘 결제 모듈이다.

고객은 메뉴를 주문하고 결제를 한 뒤, 영수증을 발행받을 수 있다.

모든 주문 및 결제, 영수증 발행은 표준 입출력을 사용하며 사전 정의된 make 명령을 이용하여 컴파일한다. ([README](https://github.com/joshua-dev/kakao-cafe/blob/master/README.md) 참고)

프로그램 구동 시 발생하는 시나리오는 다음과 같다.

1. 메뉴 정보가 출력된다.
2. 주문 안내 메세지가 출력된다.
3. 주문을 받는다. (메뉴 선택, 샷 추가 등의 옵션도 이 때 모두 선택한다.)
4. 주문 내역을 출력하고 사용자가 입력한 내용과 맞는지 Yes or No를 입력 받아 확인한다.
5. 결제 방식을 선택하고 결제를 진행한다.
6. 영수증을 출력할지 Yes or No를 입력 받아 선택하고 Yes가 입력되면 영수증을 출력한다.
7. 다음 손님을 받는다. (다시 1번으로)

(시나리오에 포함되지 않은 예외적인 상황은 아래 명세의 예외처리를 구현하거나 개발자가 추가하여 처리한다.)

#

### :heavy_exclamation_mark:(주의) 표준 개발 환경은 다음과 같다.

OS: Ubuntu 18.04 LTS

Runtime: Python>=3.6.9

Python Linter: N/A

Python Formatter: yapf 0.29.0

Test Library: unittest

**Object-Oriented-Programming 방식을 이용할 것을 권장한다.**

#

### 카페 메뉴 구현 명세

#

아래는 카페 메뉴에 대한 구현 명세이다.

카카오 카페의 메뉴는 에스프레소 메뉴, 스무디, 차, 에이드의 4가지로 나뉘며 이들은 모두 최상위 메뉴 클래스 CafeMenu를 상속한다.

최종 디렉토리 구조는 다음과 같다.

```bash
kakao-cafe
├── LICENSE
├── Makefile
├── README.md
├── com
│   ├── __init__.py
│   └── kakao
│       ├── __init__.py
│       └── cafe
│           ├── README.md
│           ├── __init__.py
│           ├── cafe.py
│           ├── menu
│           │   ├── __init__.py
│           │   ├── ade
│           │   │   ├── __init__.py
│           │   │   ├── ade.py
│           │   │   ├── lemonAde.py
│           │   │   ├── orangeAde.py
│           │   │   └── strawberryAde.py
│           │   ├── cafeMenu.py
│           │   ├── dessert
│           │   │   ├── __init__.py
│           │   │   ├── belgianWaffle.py
│           │   │   ├── dessert.py
│           │   │   ├── fruitsWaffle.py
│           │   │   ├── iceWaffle.py
│           │   │   ├── newYorkCheeseCake.py
│           │   │   ├── rainbowCheeseCake.py
│           │   │   ├── redVelvetCheeseCake.py
│           │   │   ├── tiramisuCake.py
│           │   │   └── waffle.py
│           │   ├── espresso
│           │   │   ├── __init__.py
│           │   │   ├── americano.py
│           │   │   ├── cafeMocha.py
│           │   │   ├── cappuccino.py
│           │   │   ├── caramelMacchiato.py
│           │   │   ├── espresso.py
│           │   │   ├── greenTeaLatte.py
│           │   │   ├── latte.py
│           │   │   └── vanillaLatte.py
│           │   ├── smoothie
│           │   │   ├── __init__.py
│           │   │   ├── berryBerrySmoothie.py
│           │   │   ├── pineappleSmoothie.py
│           │   │   ├── smoothie.py
│           │   │   └── yogurtSmoothie.py
│           │   └── tea
│           │       ├── __init__.py
│           │       ├── chamomileTea.py
│           │       ├── greenTea.py
│           │       ├── hibiscusTea.py
│           │       ├── iceTea.py
│           │       ├── lavenderTea.py
│           │       ├── matchaMilkTea.py
│           │       ├── milkTea.py
│           │       ├── peppermintTea.py
│           │       ├── rooibosTea.py
│           │       ├── royalMilkTea.py
│           │       └── tea.py
│           └── module
│               ├── __init__.py
│               ├── cafeWorker.py
│               ├── menuPrinter.py
│               ├── orderChecker.py
│               ├── orderTaker.py
│               ├── paymentManager.py
│               └── receiptPrinter.py
├── requirements.txt
├── testutil
│   ├── testAde.py
│   ├── testCafeMenu.py
│   ├── testDessert.py
│   ├── testEspresso.py
│   ├── testModule.py
│   ├── testSmoothie.py
│   └── testTea.py
└── venv
```

메뉴의 종류가 많으므로 각 모듈마다 단위 테스트 코드가 작성된 테스트 파일을 추가하고  
**반드시 단위 테스트가 통과된 것을 확인한 후에 다음 모듈을 구현할 것을 권장한다.**

#

아래는 추상 클래스 CafeMenu에 대한 구현 명세이다.

- 생성자: public string형 멤버 변수 name, private int형 멤버 변수 price, protected bool형 멤버 변수 iced 의 값을 type default value로 초기화한다.

  CafeMenu와 CafeMenu를 상속받는 모든 클래스에서 별도의 소멸자는 구현하지 않는다.

- name에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.

  함수 원형은 다음과 같다.

```python
from abc import ABCMeta, abstractmethod


class CafeMenu(metaclass=ABCMeta):

  # ...

  @abstractmethod
  def getName(self) -> str:
    raise NotImplementedError('Method getName not implemented')

  @abstractmethod
  def setName(self, name: str) -> None:
    raise NotImplementedError('Method setName not implemented)
```

- price에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.

  함수 원형은 다음과 같다.

```python
@abstractmethod
def getPrice(self) -> int:
  raise NotImplementedError('Method getPrice not implemented')

@abstractmethod
def setPrice(self, price: int) -> None:
  raise NotImplementedError('Method setPrice not implemented')
```

- iced에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.
  함수 원형은 다음과 같다.

```python
@abstractmethod
def isIced(self) -> bool:
  raise NotImplementedError('Method isIced not implemented')

@abstractmethod
def setIced(self) -> None:
  raise NotImplementedError('Method setIced not implemented')
```

#

아래는 추상 클래스 CafeMenu를 구현하는 concrete 클래스인 Espresso에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 shot, private string형 멤버 변수 size의 값을 각각 1.0과 'Tall'로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 2500으로 초기화한다.

  멤버 변수 isIced의 값을 False로 초기화한다.

- shot에 대한 getter와 setter

- shot을 추가할 수 있는 addShot: getter와 setter를 이용해 멤버 변수 shot의 값에 인자로 받은 amount만큼 더하고 price를 amount당 500씩 더한다.

- shot을 뺄 수 있는 subShot: getter와 setter를 이용해 멤버 변수 shot의 값에 인자로 받은 amount만큼 뺀다.

  가격 변동은 없으며 기존 shot보다 amount가 클 경우 ArithmeticError를 발생시킨다.

  이 때, 더 이상 shot을 뺄 수 없다는 내용의 메세지를 출력한다.

* size에 대한 getter와 setter

* size를 한 단계 높일 수 있는 sizeUp: getter와 setter를 이용하여 Tall이면 Grande로, Grande면 Venti로 size를 올리고 price를 500 더한다.

  size가 Venti일 경우 ValueError를 발생시킨다.

  이 때, 더 이상 size를 올릴 수 없다는 내용의 메세지를 출력한다.

- name에 대한 getter: 멤버 변수 name의 값을 반환한다.

- name에 대한 setter: 인자로 받은 string형 매개변수 name으로 멤버 변수 name을 초기화하고 return한다.

* price에 대한 getter: 멤버 변수 price의 값을 반환한다.

* price에 대한 setter: 인자로 받은 int형 매개변수 price로 멤버 변수 price를 초기화하고 return한다.

* setIced: 에스프레소는 차갑게 먹을 수 없으므로 AttributeError를 발생시킨다.

* isIced: 멤버 변수 iced가 False인지 체크하고 False라면 값을 리턴하고 True라면 AttributeError를 발생시킨다.

#

아래는 Espresso를 상속받은 클래스 Americano에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 protected int형 변수 water의 값을 350으로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 3000으로 초기화한다.

- water에 대한 getter와 setter

- isIced: iced 필드의 값을 반환한다.

- setIced: 아메리카노는 차갑게 먹을 수 있으므로 iced를 True로 초기화한다. 가격 변동은 없다.

#

아래는 Espresso를 상속받은 클래스 Latte에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 변수 milk의 값을 300으로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4000으로 초기화한다.

  멤버 변수 shot의 값을 2로 초기화한다.

- milk에 대한 getter와 setter

- isIced와 setIced

#

아래는 Latte를 상속받은 클래스 VanillaLatte에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 vanillaSyrup의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4000으로 초기화한다.

- vanillaSyrup에 대한 getter와 setter

- 바닐라 시럽을 추가할 수 있는 addVanillaSyrup: vanillaSyrup의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 200씩 더한다.

#

아래는 Latte를 상속받은 클래스 CaramelMacchiato에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 caramelSyrup의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4000으로 초기화한다.

- caramelSyrup에 대한 getter와 setter

- 카라멜 시럽을 추가할 수 있는 addCaramelSyrup: caramelSyrup의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 200씩 더한다.

#

아래는 Latte를 상속받은 클래스 Cappuccino에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 cinnamon의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4500으로 초기화한다.

  멤버 변수 milk의 값을 250으로 초기화한다.

- cinnamon에 대한 getter와 setter

- 계피향을 추가할 수 있는 addCinnamon: cinnamon의 값을 인자로 받은 amount만큼 더한다. 가격 변동은 없다.

- 계피향을 뺄 수 있는 subCinnamon: cinnamon의 값을 0으로 초기화한다. 가격 변동은 없다.

#

아래는 Latte를 상속받은 클래스 CafeMocha에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 mocha의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4000으로 초기화한다.

- mocha에 대한 getter와 setter

- 초콜렛 시럽을 추가할 수 있는 addMocha: Mocha의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 300씩 더한다.

#

아래는 Latte를 상속받은 클래스 GreenTeaLatte에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 greenTea, private int형 멤버 변수 condensedMilk의 값을 모두 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4000으로 초기화한다.

- greenTea에 대한 getter와 setter

- condensedMilk에 대한 getter와 setter

- 녹차 분말을 추가할 수 있는 addGreenTea: greenTea의 값을 인자로 받은 amount만큼 더한다. 가격 변동은 없다.

- 연유를 추가할 수 있는 addCondensedMilk: condensedMilk의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 300씩 더한다.

#

아래는 CafeMenu를 상속받은 추상 클래스 Smoothie에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 groundIce의 값을 type default value로 초기화한다.

  멤버 변수 iced의 값을 True로 초기화한다.

- groundIce에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.

#

아래는 추상 클래스 Smoothie를 상속받은 concrete 클래스 BerryBerrySmoothie에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 mixedBerry의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 5000으로 초기화한다.

  멤버 변수 groundIce의 값을 400으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- groundIce에 대한 getter와 setter

- isIced: 스무디는 뜨겁게 먹을 수 없으므로 True를 반환한다.

- setIced: 스무디는 이미 차가우므로 pass한다.

- mixedBerry에 대한 getter와 setter

- mixedBerry를 추가할 수 있는 addBerry: mixedBerry의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 Smoothie를 상속받은 concrete 클래스 PineappleSmoothie에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 pineapple의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 5000으로 초기화한다.

  멤버 변수 groundIce의 값을 400으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced: 스무디는 뜨겁게 먹을 수 없으므로 True를 반환한다.

- setIced: 스무디는 이미 차가우므로 pass한다.

- groundIce에 대한 getter와 setter

- pineapple에 대한 getter와 setter

- pineapple를 추가할 수 있는 addPineapple: pineapple의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 Smoothie를 상속받은 concrete 클래스 YogurtSmoothie에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 yogurt의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 5000으로 초기화한다.

  멤버 변수 groundIce의 값을 400으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced: 스무디는 뜨겁게 먹을 수 없으므로 True를 반환한다.

- setIced: 스무디는 이미 차가우므로 pass한다.

- groundIce에 대한 getter와 setter

- yogurt에 대한 getter와 setter

- yogurt를 추가할 수 있는 addYogurt: yogurt의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 CafeMenu를 상속받은 추상 클래스 Tea에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 water의 값을 type default value로 초기화한다.

- water에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.

#

아래는 추상 클래스 Tea를 상속받은 concrete 클래스 IceTea에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 peachPowder의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 3000으로 초기화한다.

  멤버 변수 water의 값을 300으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- water에 대한 getter와 setter

- isIced: 아이스티는 뜨겁게 먹을 수 없으므로 True를 반환한다.

- setIced: 아이스티는 이미 차가우므로 pass한다.

- peacePowder에 대한 getter와 setter

- 복숭아 분말을 추가할 수 있는 addPeachPowder: peachPowder의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 400씩 더한다.

#

아래는 추상 클래스 Tea를 상속받은 concrete 클래스 GreenTea에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 greenTea의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 3000으로 초기화한다.

  멤버 변수 water의 값을 200으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced와 setIced

- water에 대한 getter와 setter

- greenTea에 대한 getter와 setter

- 녹차 티백을 추가할 수 있는 addGreenTea: greenTea의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 Tea를 상속받은 concrete 클래스 ChamomileTea에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 chamomileTea의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 3500으로 초기화한다.

  멤버 변수 water의 값을 400으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced와 setIced

- water에 대한 getter와 setter

- chamomileTea에 대한 getter와 setter

- 카모마일 티백을 추가할 수 있는 addChamomileTea: chamomileTea의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 Tea를 상속받은 concrete 클래스 PeppermintTea에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 peppermintTea의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 3500으로 초기화한다.

  멤버 변수 water의 값을 350으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced와 setIced

- water에 대한 getter와 setter

- peppermintTea에 대한 getter와 setter

- 페퍼민트 티백을 추가할 수 있는 addPeppermintTea: peppermintTea의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 Tea를 상속받은 concrete 클래스 LavenderTea에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 lavenderTea의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 3500으로 초기화한다.

  멤버 변수 water의 값을 300으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced와 setIced

- water에 대한 getter와 setter

- lavenderTea에 대한 getter와 setter

- 라벤더 티백을 추가할 수 있는 addLavenderTea: lavenderTea의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 Tea를 상속받은 concrete 클래스 RooibosTea에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 rooibosTea의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4000으로 초기화한다.

  멤버 변수 water의 값을 300으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced와 setIced

- water에 대한 getter와 setter

- rooibosTea에 대한 getter와 setter

- 루이보스 티백을 추가할 수 있는 addRooibosTea: rooibosTea의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 700씩 더한다.

#

아래는 추상 클래스 Tea를 상속받은 concrete 클래스 HibiscusTea에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 hibiscusTea의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 3000으로 초기화한다.

  멤버 변수 water의 값을 200으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced와 setIced

- water에 대한 getter와 setter

- hibiscusTea에 대한 getter와 setter

- 히비스커스 티백을 추가할 수 있는 addHibiscusTea: hibiscusTea의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 Tea를 상속받은 추상 클래스 MilkTea에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 milk와 private int형 멤버 변수 blackTea의 값을 모두 type default value로 초기화한다.

- milk에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.

- blackTea에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.

#

아래는 추상 클래스 MilkTea를 상속받은 concrete 클래스 RoyalMilkTea에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하여 private int형 멤버 변수 royalHoney의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 5000으로 초기화한다.

  멤버 변수 milk의 값을 350으로 초기화한다.

  멤버 변수 blackTea의 값을 2로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced와 setIced

- water에 대한 getter와 setter: 밀크티에만 물이 들어가지 않으므로 pass한다.

- milk에 대한 getter와 setter

- blackTea에 대한 getter와 setter

- royalHoney에 대한 getter와 setter

- 홍차 티백을 추가할 수 있는 addBlackTea: blackTea의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

- 홍차 티백을 뺄 수 있는 subBlackTea: blackTea의 값을 인자로 받은 amount만큼 뺀다.

  가격 변동은 없으며 amount의 값이 blackTea의 값보다 큰 경우 ValueError을 발생시킨다.

  이 때, 더 이상 홍차 티백을 뺄 수 없다는 에러 메세지를 출력한다.

- 꿀을 추가할 수 있는 addRoyalHoney: royalHoney의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 1000씩 더한다.

#

아래는 추상 클래스 MilkTea를 상속받은 concrete 클래스 MatchaMilkTea에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하여 private int형 멤버 변수 matcha와 private int형 멤버 변수 condensedMilk의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4500으로 초기화한다.

  멤버 변수 milk의 값을 400으로 초기화한다.

  멤버 변수 blackTea의 값을 2로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced와 setIced

- water에 대한 getter와 setter: 밀크티에만 물이 들어가지 않으므로 pass한다.

- milk에 대한 getter와 setter

- blackTea에 대한 getter와 setter

- matcha에 대한 getter와 setter

- condensedMilk에 대한 getter와 setter

- 홍차 티백을 추가할 수 있는 addBlackTea: blackTea의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

- 홍차 티백을 뺄 수 있는 subBlackTea: blackTea의 값을 인자로 받은 amount만큼 뺀다.

  가격 변동은 없으며 amount의 값이 blackTea의 값보다 큰 경우 ValueError을 발생시킨다.

  이 때, 더 이상 홍차 티백을 뺄 수 없다는 에러 메세지를 출력한다.

- 말차 분말을 추가할 수 있는 addMatcha: matcha의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 400씩 더한다.

- 연유를 추가할 수 있는 addCondensedMilk: condensedMilk의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 CafeMenu를 상속받은 추상 클래스 Ade에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 soda의 값을 type default value로 초기화한다.

- soda에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.

#

아래는 추상 클래스 Ade를 상속받은 concrete 클래스 StrawberryAde에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 strawberry의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 3500으로 초기화한다.

  멤버 변수 soda의 값을 300으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced: 에이드는 차갑게만 마시므로 True를 반환한다.

- setIced: 에이드는 이미 차가우므로 pass한다.

- soda에 대한 getter와 setter

- strawberry에 대한 getter와 setter

- 딸기를 추가할 수 있는 addStrawberry: strawberry의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 Ade를 상속받은 concrete 클래스 LemonAde에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 lemon의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 3500으로 초기화한다.

  멤버 변수 soda의 값을 300으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced: 에이드는 차갑게만 마시므로 True를 반환한다.

- setIced: 에이드는 이미 차가우므로 pass한다.

- soda에 대한 getter와 setter

- lemon에 대한 getter와 setter

- 레몬을 추가할 수 있는 addStrawberry: lemon의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 Ade를 상속받은 concrete 클래스 OrangeAde에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 orange의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 3500으로 초기화한다.

  멤버 변수 soda의 값을 300으로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced: 에이드는 차갑게만 마시므로 True를 반환한다.

- setIced: 에이드는 이미 차가우므로 pass한다.

- soda에 대한 getter와 setter

- orange에 대한 getter와 setter

- 오렌지를 추가할 수 있는 addOrange: orange의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 CafeMenu를 상속받은 추상 클래스 Dessert에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 protected bool형 멤버 변수 melted의 값을 type default value로 초기화한다.

- isMelted: 추상 메소드로 NotImplementedError를 발생시킨다.

- 디저트를 녹일 수 있는 melt: 추상 메소드로 NotImplementedError를 발생시킨다.

#

아래는 추살 클래스 Dessert를 상속받은 concrete 클래스 NewYorkCheeseCake에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 newYorkCheese의 값을 3으로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 5000으로 초기화한다.

  멤버 변수 iced의 값을 True로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced: 케이크는 냉동 보관하므로 True를 반환한다.

- setIced: 케이크는 이미 차가우므로 pass한다.

- newYorkCheese에 대한 getter와 setter

- isMelted: melted의 값을 반환한다.

- melt: 케이크를 살짝 녹여 melted의 값을 True로 바꾼다.

#

아래는 추살 클래스 Dessert를 상속받은 concrete 클래스 TiramisuCake에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 mascapone와 private int형 멤버 변수 chocolatePowder의 값을 각각 2와 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 5500으로 초기화한다.

  멤버 변수 iced의 값을 True로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced: 케이크는 냉동 보관하므로 True를 반환한다.

- setIced: 케이크는 이미 차가우므로 pass한다.

- mascapone에 대한 getter와 setter

- chocolatePowder에 대한 getter와 setter

- isMelted: melted의 값을 반환한다.

- melt: 케이크를 살짝 녹여 melted의 값을 True로 바꾼다.

- 초코렛 파우더를 추가할 수 있는 addChocolatePowder: chocolatePowder의 값을 인자로 받은 amount만큼 더한다. 가격 변동은 없다.

#

아래는 추살 클래스 Dessert를 상속받은 concrete 클래스 RedVelvetCheeseCake에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 mascapone와 private int형 멤버 변수 redVelvetPowder의 값을 모두 2로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 6000으로 초기화한다.

  멤버 변수 iced의 값을 True로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced: 케이크는 냉동 보관하므로 True를 반환한다.

- setIced: 케이크는 이미 차가우므로 pass한다.

- mascapone에 대한 getter와 setter

- redVelvetPowder에 대한 getter와 setter

- isMelted: melted의 값을 반환한다.

- melt: 레드 벨벳 케이크는 녹이면 무너져서 비주얼이 좋지 않다. 따라서 pass한다.

- 레드 벨벳 파우더를 추가할 수 있는 addRedVelvetPowder: redVelvetPowder의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추살 클래스 Dessert를 상속받은 concrete 클래스 RainbowCheeseCake에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 mascapone의 값을 2로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 5500으로 초기화한다.

  멤버 변수 iced의 값을 True로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced: 케이크는 냉동 보관하므로 True를 반환한다.

- setIced: 케이크는 이미 차가우므로 pass한다.

- mascapone에 대한 getter와 setter

- isMelted: melted의 값을 반환한다.

- melt: 케이크를 살짝 녹여 melted의 값을 True로 바꾼다.

#

아래는 추살 클래스 Dessert를 상속받은 추상 클래스 Waffle에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 numWaffles의 값을 2로 초기화한다.

- isIced: 와플은 냉동 보관하므로 True를 반환한다.

- setIced: 와플은 이미 차가우므로 pass한다.

- numWaffles에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.

- 와플을 추가할 수 있는 addWaffle: 추상 메소드로 NotImplementedError를 발생시킨다.

#

아래는 추상 클래스 Waffle을 상속받은 concrete 클래스 BelgianWaffle에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 mapleSyrup의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 5000으로 초기화한다.

  멤버 변수 iced의 값을 True로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isMelted: melted의 값을 반환한다.

- melt: 와플을 살짝 구워 melted의 값을 True로 바꾼다.

- numWaffles에 대한 getter와 setter

- addWaffle: numWaffles의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 1000씩 더한다.

#

아래는 추상 클래스 Waffle을 상속받은 concrete 클래스 IceWaffle에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하여 public int형 멤버 변수 iceCream의 값을 2로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 6000으로 초기화한다.

  멤버 변수 iced의 값을 True로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced: 와플은 냉동 보관하므로 True를 반환한다.

- setIced: 와플은 이미 차가우므로 pass한다.

- isMelted: melted의 값을 반환한다.

- melt: 와플을 살짝 구워 melted의 값을 True로 바꾼다.

- iceCream에 대한 getter와 setter

- numWaffles에 대한 getter와 setter

- addWaffle: numWaffles의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 1000씩 더한다.

- 아이스크림을 추가할 수 있는 addIceCream: iceCream의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 500씩 더한다.

#

아래는 추상 클래스 Waffle을 상속받은 concrete 클래스 FruitsWaffle에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하여 3가지 protected int형 멤버 변수 mango, strawberry, blueberry의 값을 모두 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 6000으로 초기화한다.

  멤버 변수 iced의 값을 True로 초기화한다.

- name에 대한 getter와 setter

- price에 대한 getter와 setter

- isIced: 와플은 냉동 보관하므로 True를 반환한다.

- setIced: 와플은 이미 차가우므로 pass한다.

- isMelted: melted의 값을 반환한다.

- melt: 와플을 살짝 구워 melted의 값을 True로 바꾼다.

- mango에 대한 getter와 setter

- strawberry에 대한 getter와 setter

- blueberry에 대한 getter와 setter

- numWaffles에 대한 getter와 setter

- addWaffle: numWaffles의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 1000씩 더한다.

- 과일들을 추가할 수 있는 addFruits: mango, strawberry, blueberry의 값을 각각 인자로 받은 amount만큼 더하고 가격을 amount당 1000씩 더한다.

#

### 결제 모듈 구현 명세

#

아래는 결제 시 필요한 기능(클래스)들의 목록이다.  
이들은 모두 '카페에서 어떤 일을 한다'는 공통점이 있으므로 공통 부분을 추상화할 수 있다.  
따라서 이들은 모두 인터페이스 CafeWorker를 구현하는 클래스이며, 메인 모듈에서 인스턴스화되어 서로 상호작용하며 결제 기능을 완성한다.

1. 메뉴 목록을 출력하는 MenuPrinter
2. 주문 안내 메세지를 출력하고 주문을 받는 OrderTaker
3. 주문 목록을 출력하고 사용자가 입력한 내용과 맞는지 확인하는 OrderChecker
4. 결제 방식 목록을 출력하고 결제를 진행하는 PaymentManager
5. 영수중 출력 여부를 묻고 영수증을 출력하는 ReceiptPrinter

#

아래는 인터페이스 CafeWorker에 대한 구현 명세이다.

- 생성자 및 소멸자: CafeWorker는 인터페이스이므로 필드가 없다. 따라서 구현하지 않는다.

- Print: CafeWorker 인터페이스를 구현하는 모든 서브 클래스의 객체들은 무언가를 출력한다는 공통점이 있다.

  이는 추상 메소드로 NotImplementedError를 발생시킨다. 함수 원형은 다음과 같다.

```python
from abc import ABCMeta, abstractmethod


class CafeWorker(metaclass=ABCMeta):

# ...

  @abstractmethod
  def Print(self) -> None:
    raise NotImplementedError('Method Print not implemented')
```

#

아래는 인터페이스 CafeWorker를 구현하는 concrete 클래스 <b>MenuPrinter</b>에 대한 구현 명세이다.

- 생성자: private data structure 멤버 변수 menuList에 카카오 카페의 모든 메뉴 정보를 딕셔너리에 담아 초기화한다.

- getMenuList: self.__menuList를 dict 형태로 가져오는 method

- getMenu: cafeMenu에 포함된 객체들을 list 형태로 가져오는 method

- getEspresoo: Espresso 객체들을 list 형태로 가져오는 method 

- getAde: Ade 객체들을 list 형태로 가져오는 method

- getSmoothie: Smoothie 객체들을 list 형태로 가져오는 method

- getTea: Tea 객체들을 list 형태로 가져오는 method

- getDessert: Dessert 객체들을 list 형태로 가져오는 method

- Print: 멤버 변수 cafeMenu에 담긴 값들을 읽고 메뉴들을 종류 별로 나누어 이름과 가격을 출력한다.

#

아래는 인터페이스 CafeWorker를 구현하는 concrete 클래스 OrderTaker에 대한 구현 명세이다.

- 생성자: private list형 멤버 변수 orderList를 선언한다.(OrderChecker에게 넘겨줄 최종리스트 / 예시 참고)

- ex) 만약 손님이 에스프레소를 주문한다.
  ['Espresso', 1 ,'addShot', 2.0 ,sizeUp','Grande']
  
- private int형 멤버 변수 allPrice를 선언한다.
  (총 가격을 PaymentManager에게 넘겨줄 변수)
  
- public list형 addList를 선언한다.
  (만약 손님이 4개의 메뉴주문을 하면 메뉴 1개씩 차례대로 주문받고 최종리스트에 넣기위한 리스트)
  
- 나중에 중첩되는 추가옵션을 가진 메뉴가 또 나올 수 있기때문에 메소드로 구현하여 반복하여 추가하지 않고 불러올 수 있게 했다.

- Print: 주문 안내 메세지를 출력하고 번호를 입력하도록 한다.

------


- takeOrder 메소드에 대한 설명

1. 손님이 메뉴리스트에 있는 번호를 입력한 리스트를 받는다.
2. 리스트를 그 길이만큼 반복하여 하나씩 추출하며 1~30
   모든메뉴의 번호와 비교한다.
3. 손님이 입력한 번호와 메뉴 번호가 같으면 addList에 그 메뉴를 append 해주고, 메뉴의 추가옵션을 차례로 물어본다.
4. 공통적으로 수량을 물어본다. 그 수량만큼 allPrice에 더해준다. 수량만큼 추가옵션을 반복하여 수량에 맞고 추가옵션을 들어오도록 한다.
5. 추가옵션의 메소드에서 추가를 할건지 말건지 물어보고 추가한다면 addList에 추가옵션 name을 String형으로 append하고 얼마나 수량은 int형으로 append 추가한다. 그리고 allPrice에 (추가한 수량 X 추가 가격)을 더해준다.
6. 한 메뉴의 공통적인 addName, askMount, askIceOrHot, addAllPrice 메소드 + 추가 옵션 메소드를 실행하여 append된 addList를 최종적인 리스트 orderList에 넣어준다.
   그리고 나서 다시 처음으로 돌아가 addList와 allPrice를 초기화해준다.(다음 메뉴를 새로 추가하기 위해서)
7. orderList에 담긴 메뉴들을 사용자에게 직관적으로 출력해준다.

- 추가옵션 메소드

1. addName()
   손님이 주문한 번호를 가져와 -1 빼준다. 그 이유는 손님이 주문한 번호는 1부터 시작하고 리스트의 시작은 0부터 시작하기 때문이다. 그 수에 대한 MenuPrinter().getMenu()에 모아둔 리스트의 getName()을 addList에 넣어준다.

2. askAmount()
   손님에게 얼마만큼의 수량을 주문할지 물어보고 addList에 추가해준다.

3. askIceOrHot() , confirmIce(), confirmHot()
   아메리카노와 히비스커스 티 같은 커피와 티 종류에는 ICE와 HOT을 둘다 제조할 수 있기때문에 askIceOrHot()을 만들었고 addIce(), addHot()은 고정적으로 존재하는 메뉴에 의해 만들었다.

4. askAddshot()
   에스프레소 등과 같은 샷에 대해 추가하거나 뺄 수 있는 메뉴들을 위해 구현한 메소드. 처음에는 샷추가하거나 빼거나, 기본을 물어보고 샷추가나 뺀다고 하면 다시 샷추가, 샷빼기를 물어본다. 샷은 실수로 이어져있기 때문에 구분하기 위해 실수로 input한다.

5. askSizeUp()
   커피나 티, 스무디 같은 메뉴들을 위한 사이즈 업 메소드이다. 사이즈 업 메뉴에는 Grande, Venti 두종류로 나누어 손님에게 물어본다.

6. askGreenTea()
   그린티 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

7. askCondensedMilk()
   연유 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

8. askVanillaSyrup()
   바닐라시럽 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

9. askCafeMocha()
   카페모카 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

10. askCaramelSyrup()
    카라멜 시럽 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

11. askLemon()
    레몬 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

12. askOrange()
    오렌지 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

13. askStrawberry()
    딸기 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

14. askYogurt()
    요거트 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

15. askBerry()
    베리 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

16. askPineapple()
    파인애플 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

17. askChamomileTea()
    카모마일 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

18. askHibiscusTea()
    히비스커스 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

19. askPeachPowder()
    복숭아 파우더 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

20. askLavenderTea()
    라벤더 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

21. askBlackTea()
    블랙티 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

22. askRoyalHoney()
    로얄꿀 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

23. askMatcha()
    맛차 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

24. askPeppermintTea()
    페퍼민트 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

25. askRooibosTea()
    루이보스 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

26. askWaffle()
    와플 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

27. askFruitsMango()
    망고 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

28. askFruitsStrawberry()
    딸기 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

29. askFruitsBlueberry()
    블루베리 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

30. askIceCream()
    아이스크림 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

31. askRedVelvetPowder()
    레드벨벳 파우더 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

32. askChocolatePowder()
    초콜릿 파우더 추가옵션, 손님에게 추가, 기본을 물어보고 추가한다면 얼만큼 추가 할 지 물어본다. 그리고 그 수량만큼 addList에 추가해주고 수량 X 추가 가격을 allPrice에 넣어준다.

33. addIngredient()

    사용자가 주문한 메뉴의 추가 옵션들을 직관적으로 result에 추가해준다.

34. Character()

    사용자가 주문한 메뉴의 특징인 ICE, HOT 과 메뉴의 개수를 result에 추가해준다.

35. LoadName()

    사용자가 주문한 메뉴가 주문 가능한 메뉴인지 판별하기 위해서 Menu의 이름들을 불러온다.

36. Print2()

    사용자의 총 주문 내역을 보기 좋게 출력해 준다.

- getAllPrice 메소드: 총 가격을 paymentManager에게 넘겨주기 위해서 생성
- getOrderList: 최종적으로 넘겨줄 리스트
- getAddlist: OrderList에 append해주기 위한 리스트

------


아래는 인터페이스 CafeWorker를 구현하는 concrete 클래스 OrderChecker에 대한 구현 명세이다.

- 생성자: private str형 멤버 변수 userinput 의 값을 type default value로 초기화한다.

- Print: 사용자가 입력하기 편하도록 선을 그어 입력할 자리를 만들어준다.

- askOrderList: 주문한 내역이 맞는지 확인하고 사용자 입력을 기다린다.

  Y나 y, Yes나 yes가 입력되면 주문 내역이 올바른 것으로 간주하고 다음 단계로 넘어간다.

  N이나 n, No나 n이 입력되면 잘못된 주문이 입력된 것으로 간주하고 첫 결제 화면으로 돌아간다.

#

아래는 인터페이스 CafeWorker를 구현하는 concrete 클래스 <b>PaymentManager</b>에 대한 구현 명세이다.

- private String형 paymentSystem, private int형 cardBalance, private int형 cash, private int형 change, private int형 point를 type default로 초기화한다.
- cardBalance에 대한 setter
- cash에 대한 getter, setter
- change에 대한 getter, setter
- point에 대한 setter, getter
- selectPayment 메소드: 결제수단을 선택하는 
- cardPay 메소드: selectPayment에서 결제수단을 카드로 선택한 경우의 
- cashPay 메소드: selectPayment에서 결제수단을 현금으로 선택한 경우의 

- Print: 결제 가능한 수단들의 목록을 출력한다.



#

아래는 인터페이스 CafeWorker를 구현하는 concrete 클래스 ReceiptPrinter에 대한 구현 명세이다.

- 생성자: 

- Print: 주문한 상품의 이름, 수량 등을 영수증에 출력하고 결제수단과 받은 금액, 거스름 돈, 총 금액을 출력한다.

- printReceipt: 영수증을 출력한다.

#

### 메인 모듈

메인 모듈은 cafe.py에 main함수를 정의함으로써 구현된다.

main은 CafeWorker를 구현하는 5가지 concrete 클래스들의 객체를 인스턴스화하여 시나리오가 정상 작동하도록 한다.

#

**구현 도중 막히거나 모르는 부분이 있다면 구글링을 통해 어떻게든 알아내시길 바랍니다. ^^ :trollface:**

감사합니다.

#

귀염둥이 라이언 드림

#

Ryan

KAKAO, R&D

Mobile 010-1234-5678 Tel 070-7492-1300

cuteryan@kakao.com

경기도 성남시 분당구 판교역로 235 에이치스퀘어 N동 7층
