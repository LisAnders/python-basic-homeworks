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
    return [number ** 2 for number in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    """
    функция, которая проверяет является ли число простым

    :param number:
    :return:
    """
    if number > 1:
        for n in range(2, int(number/2)+1):
            if (number % n) == 0:
                return False
        else:
            return True
    else:
        return False


def filter_numbers(numbers_list, filter_type):
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
        return list(filter(lambda num: num % 2 != 0, numbers_list)) #[number for number in numbers_list if number % 2 != 0]
    if filter_type == EVEN:
        return list(filter(lambda num: num % 2 == 0, numbers_list)) #[number for number in numbers_list if number % 2 == 0]
    if filter_type == PRIME:
        return list(filter(is_prime, numbers_list)) #[number for number in numbers_list if is_prime(number)]
