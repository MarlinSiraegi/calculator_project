## Calculator 패키지

이 패키지는 기본 계산기와 공학용 계산기를 제공합니다. 기본 계산기 클래스인 `Calculator`는 덧셈, 뺄셈, 곱셈, 나눗셈의 기본적인 연산을 지원하며, 공학용 계산기 클래스인 `EngineeringCalculator`는 제곱근, 거듭제곱, 로그, 자연로그, 삼각함수의 계산을 추가로 지원합니다.

### 주요 기능

- **기본 계산기 (Calculator)**:
  - 덧셈, 뺄셈, 곱셈, 나눗셈을 지원합니다.
  - 소수점 자릿수를 지정할 수 있으며, 출력값을 float으로 지정할 수 있습니다.
  
- **공학용 계산기 (EngineeringCalculator)**:
  - 기본 계산기에 더해 제곱근, 거듭제곱, 로그, 삼각함수 연산을 제공합니다.
  - 삼각함수 계산 시 각도 단위를 라디안 또는 도(degree)로 선택할 수 있습니다.
  - 기존 Calculator 클래스를 상속하며, devide 메서드를 오버라이딩 합니다.

### 사용 예시

#### 기본 계산기

```python
from calculator.basic import Calculator

calc = Calculator()

print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00
print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0
print(calc.multiply(2, 3, 4))  # 출력: 24
print(calc.divide(100, 2, precision=3))  # 출력: 50.000
```

#### 공학용 계산기

```python
from calculator.engineering import EngineeringCalculator

eng_calc = EngineeringCalculator()

print(eng_calc.add(1, 2, 3, precision=2))  # 출력: 6.00
print(eng_calc.square_root(16, precision=3))  # 출력: 4.000
print(eng_calc.log(100, precision=4))  # 출력: 2.0000
print(eng_calc.sin(30, angle_units='degree', precision=4))  # 출력: 0.5000
```

### 유틸리티 함수

`utils.py` 모듈은 계산기 내부에서 사용되는 공통 함수들을 제공합니다:

- **`round_result(value, precision, return_float)`**: 주어진 값을 지정된 소수점 자리까지 반올림하고, 문자열 또는 float로 반환합니다.
- **`convert_to_radians(angle, unit)`**: 각도를 라디안으로 변환하는 함수입니다. 단위가 degree인 경우 라디안으로 변환합니다.
  
#### 사용 예시
```python
from calculator.utils import round_result, convert_to_radians

print(round_result(3.14159, precision=2))  # 출력: '3.14'
print(convert_to_radians(180, 'degree'))  # 출력: 3.141592653589793
```

### 패키지 구조

```
calculator/
├── __init__.py
├── basic.py
├── engineering.py
└── utils.py
```

- **`basic.py`**: 기본 계산기인 `Calculator` 클래스가 포함되어 있습니다.
- **`engineering.py`**: 공학용 계산기인 `EngineeringCalculator` 클래스가 포함되어 있습니다.
- **`utils.py`**: 내부적으로 사용하는 유틸리티 함수들을 포함합니다.
