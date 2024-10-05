import math
from typing import Union
from .basic import Calculator
from .utils import convert_to_radians

class DivisionByZeroError(Exception):
    pass

class EngineeringCalculator(Calculator):
    """
    ## 공학용 계산기 클래스는 제곱근, 거듭제곱, 로그, 자연로그, 삼각함수의 계산을 지원합니다.
    기존 Calculator 클래스를 상속하며, divide 메서드를 오버라이딩 합니다.

    ### 사용예시:
    from calculator.engineering import EngineeringCalculator
    eng_calc = EngineeringCalculator()  
    print(eng_calc.add(1, 2, 3, precision=2))  # 출력: 6.00  
    print(eng_calc.square_root(16, precision=3))  # 출력: 4.000  
    print(eng_calc.log(100, precision=4))  # 출력: 2.0000  
    print(eng_calc.sin(30, angle_units='degree', precision=4))  # 출력: 0.5000
    """

    def divide(self, *args: float, **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')
        result = args[0]
        for i in args[1:]:
            if i == 0:
                raise DivisionByZeroError("Division by zero is not allowed")
            else:
                result /= i
        return self.final_result(result, precision, return_float)
    
    def square_root(self, x: float, **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')
        result = x**(1/2)
        return self.final_result(result, precision, return_float)
    
    def power(self, x: float, y: float, **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')
        result = x**y
        return self.final_result(result, precision, return_float)

    def log(self, x: float, base:float = 10, **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')
        result = math.log(x,base)
        return self.final_result(result, precision, return_float)
    
    def ln(self, x: float, **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')
        result = math.log(x)
        return self.final_result(result, precision, return_float)

    def sin(self, x: float, angle_units: str ='radian', **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')
        if angle_units == 'degree':
            x = math.radians(x)
        result = math.sin(x)
        return self.final_result(result, precision, return_float)
    
    def cos(self, x: float, angle_units: str ='radian', **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')
        if angle_units == 'degree':
            x = math.radians(x)
        result = math.cos(x)
        return self.final_result(result, precision, return_float)

    def tan(self, x: float, angle_units: str ='radian', **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')
        if angle_units == 'degree':
            x = math.radians(x)
        result = math.tan(x)
        return self.final_result(result, precision, return_float)
    
    def final_result(self, result: float, precision: int = None, return_float: bool = False):
        if precision is not None:
            result = format(result, ".%df" %precision)
            return result
        else:
            if return_float:
                return round(float(result), 10)
            else:
                return int(result)