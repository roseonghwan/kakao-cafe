# Warming-Up examples

### Python virtualenv, virtualenvwrapper 설치

```shell
$ pip3 install --upgrade pip
$ pip install virtualenv virtualenvwrapper
```

### 가상환경 생성

```shell
$ virtualenv venv --python=python3
```

### 가상환경 활성화/비활성화

```shell
$ source venv/bin/activate
$ deactivate
```

### 의존성 패키지 관리

#### 현재 설치된 패키지들을 저장

```shell
$ pip freeze > requirements.txt
```

#### requirements.txt에 저장된 패키지 설치

```shell
$ pip install -r requirements.txt
```

---

## Makefile을 이용한 구동 및 테스트 단순화

### Python 단위 테스트

```shell
$ make test
$ make clean
```

### Python 구동

```shell
$ make run
```

---

### TODO

- [ ] 추상 클래스 CafeMenu 구현 및 테스트 코드 작성
#
- [ ] Espresso 클래스 구현 및 테스트 코드 작성
- [ ] Americano 클래스 구현 및 테스트 코드 작성
- [ ] Latte 클래스 구현 및 테스트 코드 작성
- [ ] VanillaLatte 클래스 구현 및 테스트 코드 작성
- [ ] CaramelMacchiato 클래스 구현 및 테스트 코드 작성
- [ ] Cappucino 클래스 구현 및 테스트 코드 작성
- [ ] CafeMocha 클래스 구현 및 테스트 코드 작성
#
- [ ] 추상 클래스 Smoothie 구현 및 테스트 코드 작성
- [ ] BerryBerrySmoothie 클래스 구현 및 테스트 코드 작성
- [ ] PineappleSmoothie 클래스 구현 및 테스트 코드 작성
- [ ] YogurtSmoothie 클래스 구현 및 테스트 코드 작성
#
- [ ] 추상 클래스 Tea 구현 및 테스트 코드 작성
- [ ] IceTea 클래스 구현 및 테스트 코드 작성
- [ ] GreenTea 클래스 구현 및 테스트 코드 작성
- [ ] ChamomileTea 클래스 구현 및 테스트 코드 작성
- [ ] PeppermintTea 클래스 구현 및 테스트 코드 작성
- [ ] LavenderTea 클래스 구현 및 테스트 코드 작성
- [ ] RooibosTea 클래스 구현 및 테스트 코드 작성
- [ ] HibiscusTea 클래스 구현 및 테스트 코드 작성
- [ ] 추상 클래스 MilkTea 구현 및 테스트 코드 작성
- [ ] RoyalMilkTea 클래스 구현 및 테스트 코드 작성
- [ ] MatchaMilkTea 클래스 구현 및 테스트 코드 작성
#
- [ ] 추상 클래스 Ade 구현 및 테스트 코드 작성
- [ ] StrawberryAde 클래스 구현 및 테스트 코드 작성
- [ ] LemonAde 클래스 구현 및 테스트 코드 작성
- [ ] OrangeAde 클래스 구현 및 테스트 코드 작성
#
- [ ] 테스트 코드 추상화
