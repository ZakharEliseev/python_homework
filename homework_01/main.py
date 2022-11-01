"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [numbers ** 2 for numbers in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

a = 3
def is_prime(a):
    if a > 1:
        for n in range(2, int(a / 2) + 1):
            if (a % n) == 0:
                return print(False)

        else:
            return print(True)
    else:
        return print(False)


def filter_numbers(number_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return [number for number in number_list if number % 2 != 0]
    if filter_type == EVEN:
        return [number for number in number_list if number % 2 == 0]
    if filter_type == PRIME:
        return is_prime()
