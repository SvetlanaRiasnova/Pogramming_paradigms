#Декларативная
#- используете готовый функционал
#- исполнение “под капотом”
#- текст вашей программы “близок” к
#конечному результату


# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
# Пример процедуры для сортировки списка чисел в порядке убывания, используя алгоритм сортировки выбором:

from random import randint
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:

    return sorted(arr, reverse=True)


numbers = [randint(0, 100) for i in range(7)]
print(numbers)
print(bubble_sort(numbers))