# 계산기 프로젝트 (Calculator Project)

Python을 이용해 **기본 계산기**와 **공학용 계산기**를 제공하는 패키지입니다. 기본 계산기 클래스인 `Calculator`는 덧셈, 뺄셈, 곱셈, 나눗셈의 기본적인 연산을 지원하며, 공학용 계산기 클래스인 `EngineeringCalculator`는 추가적인 수학 연산 기능을 제공합니다.

## 주요 기능

### 기본 계산기 (`Calculator`)
- **기본 연산**: 덧셈, 뺄셈, 곱셈, 나눗셈을 지원합니다.
- **소수점 자리수 지정**: 결과의 소수점 자릿수를 지정할 수 있으며, 출력값을 **float**으로 설정할 수 있습니다.

### 공학용 계산기 (`EngineeringCalculator`)
- **기본 계산기 기능**: `Calculator` 클래스를 상속하여 기본 연산을 제공합니다.
- **추가 연산 기능**:
  - **제곱근**, **거듭제곱**, **로그**, **자연로그**.
  - **삼각함수**: sin, cos, tan 계산을 지원하며, **라디안** 또는 **도(degree)** 단위를 사용할 수 있습니다.
- **메서드 오버라이딩**: 나눗셈 메서드(`divide`)를 오버라이딩하여 `0`으로 나누는 경우 오류를 처리합니다.

### 유틸리티 함수
- **정밀도 설정**: 주어진 값을 지정된 소수점 자리까지 반올림하고, 문자열 또는 float로 반환합니다.
- **각도를 라디안으로 변경**: 각도를 라디안으로 변환하는 함수로, 단위가 degree인 경우 라디안으로 변환합니다.

## 사용 예시

### 기본 계산기
```python
from calculator.basic import Calculator

calc = Calculator()

print(calc.add(1, 2, 3, precision=2))  # 출력: '6.00'
print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0
print(calc.multiply(2, 3, 4))  # 출력: 24
print(calc.divide(100, 2, precision=3))  # 출력: '50.000'
```

### 공학용 계산기
```python
from calculator.engineering import EngineeringCalculator

eng_calc = EngineeringCalculator()

print(eng_calc.add(1, 2, 3, precision=2))  # 출력: '6.00'
print(eng_calc.square_root(16, precision=3))  # 출력: '4.000'
print(eng_calc.log(100, precision=4))  # 출력: '2.0000'
print(eng_calc.sin(30, angle_units='degree', precision=4))  # 출력: '0.5000'
```

### 유틸리티 함수
```python
from calculator.utils import round_result, convert_to_radians

print(round_result(3.14159, precision=2))  # 출력: '3.14'
print(convert_to_radians(180, 'degree'))  # 출력: 3.141592653589793
```

## 프로젝트 구조

```
calculator_project/
├── calculator/
│   ├── __init__.py
│   ├── basic.py
│   ├── engineering.py
│   ├── utils.py
│   └── README.md
├── tests/
│   ├── __init__.py
│   ├── test_basic.py
│   ├── test_engineering.py
│   └── test_utils.py
├── LICENSE.txt
├── README.md
├── setup.py
└── .gitignore
```

- **`calculator/`**: 계산기 모듈이 포함된 디렉토리입니다 (`basic.py`, `engineering.py`, `utils.py`).
- **`tests/`**: 각 계산기 모듈에 대한 테스트 코드가 포함된 디렉토리입니다.
- **`LICENSE.txt`**: 프로젝트의 라이선스 파일입니다.
- **`README.md`**: 프로젝트 설명서 파일입니다.
- **`setup.py`**: 패키지 설치와 관련된 설정 파일입니다.