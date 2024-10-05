import math

def round_result(value: float, precision: int = None, return_float: bool = False) -> float:
    """
    결과값을 지정된 정밀도로 반올림하는 함수
    """
    if precision is not None:
        result = round(value, precision)
        return f"{result:.{precision}f}" if not return_float else result
    return int(value) if not return_float else round(value, 10)

def convert_to_radians(angle: float, unit: str = 'radian') -> float:
    """
    각도를 라디안으로 변환하는 함수
    """
    if unit == 'degree':
        return math.radians(angle)
    return angle