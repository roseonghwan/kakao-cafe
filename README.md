# Warming-Up examples.

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
