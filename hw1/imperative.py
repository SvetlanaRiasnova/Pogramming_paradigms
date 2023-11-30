# Императивная
# - пишете математические операции
# - описываете команды на уровне 
# конкретных переменных
# - имеете доступ к памяти
from random import randint
from typing import List

# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


def bubble_sort(arr: List[int]) -> List[int]:
    """Метод сортировки списка пузырьком.
   Пошагово прописываем алгоритм, который будет выполняться, пока массив не будет отсортирован"""

    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1):
            if (arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


numbers = [randint(0, 100) for i in range(7)]
print(numbers)
print(bubble_sort(numbers))