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

메뉴의 종류가 많으므로 각 모듈마다 단위 테스트 코드가 작성된 테스트 파일을 추가하고 **반드시 단위 테스트가 통과된 것을 확인한 후에 다음 모듈을 구현할 것을 권장한다.**

#

아래는 추상 클래스 CafeMenu에 대한 구현 명세이다.

- 생성자: public string형 멤버 변수 name, private int형 멤버 변수 price, protected bool형 멤버 변수 iced 의 값을 type default value로 초기화한다.

  CafeMenu와 CafeMenu를 상속받는 모든 클래스에서 별도의 소멸자는 구현하지 않는다.

- name에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.

  함수 원형은 다음과 같다.

```python
from abc import *


class CafeMenu(metaclass=ABCMeta):

  # ...

  @abstractmethod
  def getName(self) -> str:
    raise NotImplementedError

  @abstractmethod
  def setName(self, name: str) -> None:
    raise NotImplementedError
```

- price에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.

  함수 원형은 다음과 같다.

```python
@abstractmethod
def getPrice(self) -> int:
  raise NotImplementedError

@abstractmethod
def setPrice(self, price: int) -> None:
  raise NotImplementedError
```

- iced에 대한 getter와 setter: 추상 메소드로 NotImplementedError를 발생시킨다.
  함수 원형은 다음과 같다.

```python
@abstractmethod
def isIced(self) -> bool:
  raise NotImplementedError

@abstractmethod
def setIced(self) -> None:
  raise NotImplementedError
```

#

아래는 추상 클래스 CafeMenu를 구현하는 concrete 클래스인 Espresso에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private float형 멤버 변수 shot, private string형 멤버 변수 size의 값을 각각 1.0과 'Tall'로 초기화한다.

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
from abc import *


class CafeWorker(metaclass=ABCMeta):

# ...

  @abstractmethod
  def Print(self) -> None:
    raise NotImplementedError
```

#

아래는 인터페이스 CafeWorker를 구현하는 concrete 클래스 MenuPrinter에 대한 구현 명세이다.

- 생성자: private data structure 멤버 변수 cafeMenu에 카카오 카페의 모든 메뉴 정보를 **가장 적합한 자료구조**에 담아 초기화한다.

- Print: 멤버 변수 cafeMenu에 담긴 값들을 읽고 메뉴들을 종류 별로 나누어 이름과 가격을 출력한다.

#

아래는 인터페이스 CafeWorker를 구현하는 concrete 클래스 OrderTaker에 대한 구현 명세이다.

- 생성자:

- Print:

#

아래는 인터페이스 CafeWorker를 구현하는 concrete 클래스 OrderChecker에 대한 구현 명세이다.

- 생성자:

- Print:

#

아래는 인터페이스 CafeWorker를 구현하는 concrete 클래스 PaymentManager에 대한 구현 명세이다.

- 생성자:

- Print:

#

아래는 인터페이스 CafeWorker를 구현하는 concrete 클래스 ReceiptPrinter에 대한 구현 명세이다.

- 생성자:

- Print:

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
