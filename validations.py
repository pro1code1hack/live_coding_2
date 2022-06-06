from typing import List


def task_1validation(AB: List[tuple], CD: List[tuple]) -> bool:
    """The function validates the input data in order to proceed with binary search"""
    if not isinstance(AB, List) or not isinstance(CD, List):
        raise TypeError('Input data must be list')
    if len(AB) != 2 or len(CD) != 2:
        raise ValueError('Input data must be list with 2 elements')
    if not isinstance(AB[0], tuple) or not isinstance(AB[1], tuple) or not isinstance(CD[0], tuple) or not isinstance(
            CD[1], tuple):
        raise TypeError('Input data must be list with 2 tuples')
    if len(AB[0]) != 2 or len(AB[1]) != 2 or len(CD[0]) != 2 or len(CD[1]) != 2:
        raise ValueError('Input data must be list with 2 tuples with 2 elements')
    return True

def task_2validation(arr: list, value: int) -> bool:
    """The function validates the input data in order to proceed with binary search"""
    if not isinstance(arr, list):
        raise TypeError('Input data must be list')
    if len(arr) == 0:
        raise ValueError('Input data must be not empty list')
    if not isinstance(value, int):
        raise TypeError('Input data must be int')
    if value < 0:
        raise ValueError('Input data must be positive')
    if value > max(arr):
        raise ValueError('Input data must be less than max value in list')
    return True