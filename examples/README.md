# 카페 주문 시스템 구현

안녕하세요, 카카오 신입 크루 여러분.

경영본부의 귀여움을 담당하고 있는 라이언입니다.

카카오는 다가오는 봄을 맞아 '카카오 카페' 시스템을 구축하기로 했습니다.

'카카오 카페'는 카카오의 야심찬 신년 프로젝트로, 전국의 카페 매장들을 타겟으로 하는 대규모 결제 플랫폼 프로젝트의 일환입니다.

올해 6월까지 카카오 페이, 카카오 뱅크 등과 연동하여 카카오 플랫폼에 포함시켜 상용화할 예정이며, 예상 수익은 연 1200억원으로 추정하고 있습니다.

현재 개발 책임팀에서 최종 설계를 디자인 중이며, 신입 개발팀은 아래의 API 명세에 따라 코드를 구현해주시면 됩니다.

---

카카오 카페는 카페 메뉴 정보와 결제 및 영수중 발행까지의 기능을 갖춘 결제 시스템이다.

고객은 메뉴를 주문하고 결제를 한 뒤, 영수증을 발행받을 수 있다.

POS기가 아직 미구비 상태인 관계로 모든 주문 및 결제, 영수증 발행은 표준 입출력을 사용하며 Makefile의 커맨드를 이용하여 컴파일한다. ([README](https://github.com/joshua-dev/warmingup/blob/master/README.md) 참고)

---

### (주의) 개발 표준은 다음과 같다.

Runtime: Python>=3.6.9

Python Linter: N/A

Python Formatter: yapf 0.29.0

Test Library: unittest

**Object-Oriented-Programming 방식을 이용할 것을 권장합니다.**

---

아래는 카페 메뉴에 대한 구현 명세이다.

카카오 카페의 카페 메뉴는 에스프레소 메뉴, 스무디, 차, 에이드의 4가지로 나뉘며 이들은 모두 최상위 메뉴 클래스 CafeMenu를 상속한다.

메뉴의 종류가 많으므로 각 모듈마다 단위 테스트 코드가 작성된 테스트 파일을 추가하고 **반드시 단위 테스트가 통과된 것을 확인한 후에 다음 모듈을 구현할 것을 권장한다.**

---

아래는 추상 클래스 CafeMenu에 대한 구현 명세이다.

- 생성자: public string형 멤버 변수 name, private int형 멤버 변수 price, private bool형 멤버 변수 iced 의 값을 type default value로 초기화한다.

  CafeMenu와 CafeMenu를 상속받은 클래스에서 별도의 소멸자는 구현하지 않는다.

- name에 대한 setter: 인자로 받은 name을 멤버 변수 name에 저장한다.

- name에 대한 getter: 자신의 멤버 변수 name의 값을 반환한다.

- price에 대한 setter와 getter: 추상 메소드로 NotImplementedError를 발생시킨다.

  함수 원형은 다음과 같다.

```python
from abc import ABC, abstractmethod

# ...

@abstractmethod
def setPrice(self, price: int) -> None:
  raise NotImplementedError()

@abstractmethod
def getPrice(self) -> int:
  raise NotImplementedError()
```

- iced에 대한 setter와 getter: 추상 메소드로 NotImplementedError를 발생시킨다.
  함수 원형은 다음과 같다.

```python
@abstractmethod
def setIced(self) -> None:
  raise NotImplementedError()

@abstractmethod
def isIced(self) -> bool:
  raise NotImplementedError()
```

---

아래는 추상 클래스 CafeMenu를 구현하는 concrete 클래스인 Espresso에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private float형 멤버 변수 shot, private string형 멤버 변수 size의 값을 각각 1.0과 'Tall'로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 2500으로 초기화한다.

- shot에 대한 setter와 getter

- shot을 추가할 수 있는 addShot: setter와 getter를 이용해 멤버 변수 shot의 값에 인자로 받은 amount만큼 더하고 price를 amount당 500씩 더한다.

- shot을 뺄 수 있는 subShot: setter와 getter를 이용해 멤버 변수 shot의 값에 인자로 받은 amount만큼 뺀다.

  가격 변동은 없으며 기존 shot보다 amount가 클 경우 ArithmeticError를 발생시킨다.

  이 때, 더 이상 shot을 뺄 수 없다는 내용의 메세지를 출력한다.

* size에 대한 setter와 getter

* size를 한 단계 높일 수 있는 sizeUp: setter와 getter를 이용하여 Tall이면 Grande로, Grande면 Venti로 size를 올리고 price를 500 더한다.

  size가 Venti일 경우 ValueError를 발생시킨다.

  이 때, 더 이상 size를 올릴 수 없다는 내용의 메세지를 출력한다.

* price에 대한 setter: 인자로 받은 int형 매개변수 price로 멤버 변수 price를 초기화하고 return한다.

* price에 대한 getter: 멤버 변수 price의 값을 반환한다.

* setIced: 에스프레소는 차갑게 먹을 수 없으므로 AttributeError를 발생시킨다.

* isIced: False를 반환한다.

---

아래는 Espresso를 상속받은 클래스 Americano에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 protected int형 변수 water의 값을 350으로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 3000으로 초기화한다.

- water에 대한 setter와 getter

- setIced: 아메리카노는 차갑게 먹을 수 있으므로 iced를 True로 초기화한다. 가격 변동은 없다.

- isIced: iced 필드의 값을 반환한다.

---

아래는 Espresso를 상속받은 클래스 Latte에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 변수 milk의 값을 300으로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4000으로 초기화한다.

  멤버 변수 shot의 값을 2로 초기화한다.

- milk에 대한 setter, getter

- setIced와 isIced

---

아래는 Latte를 상속받은 클래스 VanillaLatte에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 vanillaSyrup의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4000으로 초기화한다.

- vanillaSyrup에 대한 getter와 setter

- 바닐라 시럽을 추가할 수 있는 addVanillaSyrup: vanillaSyrup의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 200씩 더한다.

---

아래는 Latte를 상속받은 클래스 CaramelMacchiato에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 caramelSyrup의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4000으로 초기화한다.

- caramelSyrup에 대한 getter와 setter

- 카라멜 시럽을 추가할 수 있는 addCaramelSyrup: caramelSyrup의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 200씩 더한다.

---

아래는 Latte를 상속받은 클래스 Cappuccino에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 cinnamon의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4500으로 초기화한다.

  멤버 변수 milk의 값을 250으로 초기화한다.

- cinnamon에 대한 getter와 setter

- 계피향을 추가할 수 있는 addCinnamon: cinnamon의 값을 인자로 받은 amount만큼 더한다. 가격 변동은 없다.

- 계피향을 뺄 수 있는 subCinnamon: cinnamon의 값을 0으로 초기화한다. 가격 변동은 없다.

---

아래는 Latte를 상속받은 클래스 CafeMocha에 대한 구현 명세이다.

- 생성자: 부모 클래스의 생성자를 호출하며 private int형 멤버 변수 mocha의 값을 1로 초기화한다.

  멤버 변수 name의 값을 클래스 이름과 동일하게 초기화한다.

  멤버 변수 price의 값을 4000으로 초기화한다.

- mocha에 대한 getter와 setter

- 초콜렛 시럽을 추가할 수 있는 addMocha: Mocha의 값을 인자로 받은 amount만큼 더하고 가격을 amount당 300씩 더한다.

---

아래는 추상 클래스 Smoothie에 대한 구현 명세이다.

- 생성자:

---

**구현 도중 막히거나 모르는 부분이 있다면 구글링을 통해 어떻게든 알아내시길 바랍니다. ^^**

감사합니다.

귀염둥이 라이언 드림

Ryan

KAKAO, R&D

Mobile 010-1234-5678 Tel 070-7492-1300

cuteryan@kakao.com

경기도 성남시 분당구 판교역로 235 에이치스퀘어 N동 7층