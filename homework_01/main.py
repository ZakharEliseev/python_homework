"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    num_list = []
    for num in nums:
        if num != num ** 2:
            num_list.append(num ** 2)
    return num_list


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(a):
    if a > 1:
        for n in range(2, int(a / 2) + 1):
            if (a % n) == 0:
                return False
        else:
            return True
    else:
        return False


def is_odd(*nums):
    odd_list = []
    for i in nums:
        if i % 2 != 0:
            odd_list.append(i)
    return list(odd_list)


def is_even(*nums):
    even_list = []
    for i in nums:
        if i % 2 == 0:
            even_list.append(i)
    return list(even_list)


def filter_numbers(nums, filter_type):
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
        return list(filter(is_odd, nums))
    elif filter_type == EVEN:
        return list(filter(is_even, nums))
    else:
        return list(filter(is_prime, nums))

