"""
----------------------------------------------------TASK 1----------------------------------------------------
На координатній прямій задано два відрізки: AB і CD.
Написати умову, яка визначає, чи вони перетинаються (мають хоча б одну спільну точку).
"""
import random
from typing import List

from validations import task_2validation, task_1validation

print('----------------------------------------------------TASK 1----------------------------------------------------')
def task_1(AB: List[tuple], CD: List[tuple]) -> bool:
    if not task_1validation(AB, CD):
        return False
    # Перевірка на перетин
    return True if AB[0][0] <= CD[1][0] <= AB[1][0] or AB[0][0] <= CD[0][0] <= AB[1][0] else False


print(task_1(AB=[(1, 1), (2, 2)], CD=[(2, 'asf'), (3, 3)]))
print(task_1(AB=[(12, 14), (22, 21)], CD=[(3, 3), (4, 4)]))
print(task_1(AB=[(1, 1), (2, 2)], CD=[(2, 2), (3, 3)]))

print('----------------------------------------------------TASK 2----------------------------------------------------')
"""
----------------------------------------------------TASK 2----------------------------------------------------
Написати функцію бінарного пошуку (пошуку індекса елемента у відсортованому масиві)
"""


def binary_search(arr: list, value: int) -> int:
    # Початкові значення
    if not task_2validation(arr, value):
        return -1
    left = 0
    right = len(arr) - 1
    print("left: {}, right: {}".format(left, right))
    print("arr: {}".format(arr))
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == value:
            return middle
        elif arr[middle] < value:
            left = middle + 1
        else:
            right = middle - 1
    return -1


print(binary_search(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], value=5))
print(binary_search(sorted([random.randint(-10, 20) for _ in range(20)]), 5))
print(binary_search(sorted([random.randint(-10, 5) for _ in range(20)]), 2))
