# 카카오의 신입 개발자가 된 존나팸!

# OT가 끝난 직후 한통의 [메일](https://github.com/joshua-dev/kakao-cafe/blob/master/com/kakao/cafe/README.md)을 받게 되는데...

![Thumbnail](https://t1.daumcdn.net/tvpot/thumb/v0431dmoadPdi6PH44oFHci/thumb.png?time=1490071671642)

#

[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/joshua-dev/kakao-cafe/blob/master/LICENSE)
[![Slack](https://img.shields.io/badge/chat%20on-Slack-53185A)](https://jonnafamily.slack.com/)
[![Notion](https://img.shields.io/badge/spec-Notion-51525A)](https://www.notion.so/jonnafamily/OOP-Practice-024aa342c3174aff9f35415f8a79b72d)

#

## :pushpin: Tips

### Python virtualenv, virtualenvwrapper 설치

```bash
$ pip3 install --upgrade pip
$ pip install virtualenv virtualenvwrapper
```

### 가상환경 생성

```bash
$ virtualenv venv --python=python3
```

### 가상환경 활성화/비활성화

- #### 활성화

  ```bash
  $ source venv/bin/activate
  ```

- #### 비활성화
  ```bash
  (venv) $ deactivate
  ```

---

### 의존성 패키지 관리

- #### 현재 설치된 패키지들을 저장

  ```bash
  (venv) $ pip freeze > requirements.txt
  ```

- #### requirements.txt에 저장된 패키지 설치

  ```bash
  (venv) $ pip install -r requirements.txt
  ```

---

### make를 이용한 구동 및 테스트 단순화

- #### Python 구동

  ```bash
  (venv) $ make run
  ```

- #### Python 단위 테스트

  - 모든 테스트 실행
    
    ```bash
    (venv) $ make
    ```

    ```bash
    (venv) $ make test
    ```

  - CafeMenu 테스트

    ```bash
    (venv) $ make test cafemenu
    ```

  - Espresso 및 하위 클래스 테스트

    ```bash
    (venv) $ make test espresso
    ```

  - Smoothie 및 하위 클래스 테스트
  
    ```bash
    (venv) $ make test smoothie
    ```

  - Tea 및 하위 클래스 테스트

    ```bash
    (venv) $ make test tea
    ```

  - Ade 및 하위 클래스 테스트
  
    ```bash
    (venv) $ make test ade
    ```

  - Dessert 및 하위 클래스 테스트

    ```bash
    (venv) $ make test dessert
    ```

  - Module 및 구현 클래스 테스트

    ```bash
    (venv) $ make test module
    ```

#

## :white_check_mark: TODO

#### 카페 메뉴 클래스

- [x] 추상 클래스 CafeMenu 구현 및 테스트 코드 작성

#

- [x] Espresso 클래스 구현 및 테스트 코드 작성
- [x] Americano 클래스 구현 및 테스트 코드 작성
- [x] Latte 클래스 구현 및 테스트 코드 작성
- [x] VanillaLatte 클래스 구현 및 테스트 코드 작성
- [x] CaramelMacchiato 클래스 구현 및 테스트 코드 작성
- [x] Cappuccino 클래스 구현 및 테스트 코드 작성
- [x] CafeMocha 클래스 구현 및 테스트 코드 작성
- [x] GreenTeaLatte 클래스 구현 및 테스트 코드 작성

#

- [x] 추상 클래스 Smoothie 구현 및 테스트 코드 작성
- [x] BerryBerrySmoothie 클래스 구현 및 테스트 코드 작성
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

- [x] 추상 클래스 Ade 구현 및 테스트 코드 작성
- [x] StrawberryAde 클래스 구현 및 테스트 코드 작성
- [x] LemonAde 클래스 구현 및 테스트 코드 작성
- [x] OrangeAde 클래스 구현 및 테스트 코드 작성

#

- [x] 추상 클래스 Dessert 구현 및 테스트 코드 작성
- [x] NewYorkCheeseCake 클래스 구현 및 테스트 코드 작성
- [x] TiramisuCake 클래스 구현 및 테스트 코드 작성
- [x] RedVelvetCheeseCake 클래스 구현 및 테스트 코드 작성
- [x] RainbowCheeseCake 클래스 구현 및 테스트 코드 작성
- [x] 추상 클래스 Waffle 구현 및 테스트 코드 작성
- [x] BelgianWaffle 클래스 구현 및 테스트 코드 작성
- [x] IceWaffle 클래스 구현 및 테스트 코드 작성
- [x] FruitsWaffle 클래스 구현 및 테스트 코드 작성

#

- [ ] Branch 간 Merge 및 Comflict 해결

#### 결제 모듈 클래스

- [ ] 인터페이스 CafeWorker 구현 및 테스트 코드작성
- [ ] MenuPrinter 클래스 구현 및 테스트 코드 작성
- [ ] OrderTaker 클래스 구현 및 테스트 코드 작성
- [ ] OrderChecker 클래스 구현 및 테스트 코드 작성
- [ ] PaymentManager 클래스 구현 및 테스트 코드 작성
- [ ] ReceiptPrinter 클래스 구현 및 테스트 코드 작성
- [ ] 메인 모듈 구현

#### 기타

- [ ] 예외 처리
- [ ] 테스트 코드 추상화
- [ ] 디자인 패턴과 Code Refactoring
  - Factory pattern
  - Iterator pattern
  - Composite pattern
- [ ] 함수형 프로그래밍과 고계 함수

#### 추가 기능

- [ ] 결제 정보 저장
- [ ] 매출 통계
- [ ] GUI
- [ ] 시즌 한정 메뉴
- [ ] 영업 시간

#

## :octocat: Git

#### Git config settings

<pre>
$ git config --global user.name <b><i>"Your Name"</i></b>
$ git config --global user.email <b><i>"you@your-domain.com"</i></b>
$ git config --global core.precomposeunicode true
$ git config --global core.quotepath false
</pre>

#### Git 프로젝트 디렉토리 생성 및 원격 저장소 연결

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

#### Git branch 변경

<pre>
$ git checkout <b><i>YOUR_BRANCH_NAME</i></b>
</pre>

#### 현재 Git 레포지토리 상태 확인

```bash
$ git fetch
```

#### 현재 Git 디렉토리 상태 확인

```bash
$ git status
```

#### Git에 커밋하기

<pre>
$ git add .
$ git commit -m <b><i>"COMMIT_MESSAGE"</i></b>
$ git push origin <b><i>YOUR_BRANCH_NAME</i></b>
</pre>

---

### [LICENSE](https://github.com/joshua-dev/kakao-cafe/blob/master/LICENSE)
