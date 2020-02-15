# 카카오 신입 개발자가 된 존나팸!

# OT가 끝난 직후 한통의 [메일](https://github.com/joshua-dev/warmingup/blob/master/examples/README.md)을 받게 되는데...

![thumbnail](https://t1.daumcdn.net/tvpot/thumb/v0431dmoadPdi6PH44oFHci/thumb.png?time=1490071671642)

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

### Makefile을 이용한 구동 및 테스트 단순화

#### Python 단위 테스트

```shell
$ make test
$ make clean
```

#### Python 구동

```shell
$ make run
```

### TODO

#### 카페 메뉴 클래스

- [ ] 추상 클래스 CafeMenu 구현 및 테스트 코드 작성

#

- [ ] Espresso 클래스 구현 및 테스트 코드 작성
- [ ] Americano 클래스 구현 및 테스트 코드 작성
- [ ] Latte 클래스 구현 및 테스트 코드 작성
- [ ] VanillaLatte 클래스 구현 및 테스트 코드 작성
- [ ] CaramelMacchiato 클래스 구현 및 테스트 코드 작성
- [ ] Cappuccino 클래스 구현 및 테스트 코드 작성
- [ ] CafeMocha 클래스 구현 및 테스트 코드 작성
- [ ] GreenTeaLatte 클래스 구현 및 테스트 코드 작성

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

- [ ] Commit 내용 통합 및 Comflict 해결

#### 입출력 처리 클래스

- [ ] 메뉴판 출력 클래스 구현 및 테스트 코드 작성
- [ ] 주문 기능 클래스 구현 및 테스트 코드 작성
- [ ] 영수증 출력 클래스 구현 및 테스트 코드 작성
- [ ] main 클래스 구현

#### 기타

- [ ] 예외 처리
- [ ] 테스트 코드 추상화

#### 추가 기능

- [ ] 결제 정보 저장
- [ ] 매출 통계
- [ ] GUI
- [ ] 시즌 한정 메뉴

#

### Git

#### Git 프로젝트 디렉토리 생성

<pre>
$ mkdir <b><i>YOUR_DIRECTORY_NAME</i></b>
$ cd <b><i>YOUR_DIRECTORY_NAME</i></b>
$ git init
$ git remote add origin <b><i>YOUR_GIT_REPOSITORY_ADDRESS</i></b>
$ git pull origin master
</pre>

#### Git branch 생성

<pre>
$ git branch <b><i>YOUR_BRANCH_NAME</i></b>
</pre>

#### 현재 Git 레포지토리 상태 확인

```shell
$ git fetch
```

#### 현재 Git 디렉토리 상태 확인

```shell
$ git status
```

#### Git에 커밋하기

<pre>
$ git add .
$ git commit -m <b><i>"COMMIT_MESSAGE"</i></b>
$ git push origin <b><i>YOUR_BRANCH_NAME</i></b>
</pre>
