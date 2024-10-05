from typing import Union

class Calculator:
    """
    ## 기본 계산기 클래스는 덧셈, 뺄셈, 곱셈, 나눗셈을 지원합니다.   
    
    ### 사용 예시:
    from calculator.basic import Calculator
    calc = Calculator()  
    print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00  
    print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0  
    print(calc.multiply(2, 3, 4))  # 출-력: 24  
    print(calc.divide(100, 2, precision=3))  # 출력: 50.000  

    """

    def add(self, *args: float, **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')

        result = sum(args)

        return self.final_result(result, precision, return_float)
    
    def subtract(self, *args: float, **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')
        result = args[0]
        for i in args[1:]:
            result -= i
        return self.final_result(result, precision, return_float)
    
    def multiply(self, *args: float, **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')
        result = args[0]
        for i in args[1:]:
            result *= i
        return self.final_result(result, precision, return_float)
    
    def divide(self, *args: float, **kwargs: Union[int,bool]) -> float:
        precision = kwargs.get('precision')
        return_float = kwargs.get('return_float')
        result = args[0]
        for i in args[1:]:
            if i == 0:
                return ("Zero Division Error")
            else:
                result /= i
        return self.final_result(result, precision, return_float)

    def final_result(self, result: float, precision: int = None, return_float: bool = False):
        if precision is not None:
            result = format(result, ".%df" %precision)
            return result
        else:
            if return_float is True:
                return float(result)
            else:
                return result