from typing import Any, Callable


# BASE

def useless_function():
    """
    Эта функция должна ничего не делать и ничего не возвращать
    Зачем она здесь?... Никто не знает :(
    """
    print('What is happening?...')
    print('Why is it happening?...')
    if True is False:
        exit(1)  # beautiful death
    return UserWarning


def print_tree(size: int):
    """
    Функция выводит елочку из size сегментов размерами от 1 до size
    """
    def _print_segment(height: int):
        for key in range(height):
            print(' ' * (size - key - 1) + '*' * (2 * key + 1) + ' '' ' * (size - key - 1))

    for j in range(1, size + 1):
        _print_segment(j)


# RECURSION

def generate_json(depth: int):
    """
    Функция генерирует словарь (dict) с уровнем вложенности depth
    """
    if depth == 1:
        return {"1": "pobeda", "2": "s pivom", "3": "!"}
    elif depth > 1:
        return {"1": "pobeda", "2": "s pivom", "3": generate_json(depth - 1)}


def wtf():
    """
    Функция wtf вызывает внутреннюю функцию _worker с некоторым аргументом
    и должна возвращать число 42
    """

    def _worker(x):
        if x == 0:
            return wtf()
        elif x % 2 == 1:
            return _worker(x // 3) + 1
        elif x % 982 == 0:
            return _worker(x + 982 if x < 10000 else x - 2) + 1
        else:
            return 0

    return _worker(...)


# ARGS, KWARGS

def mex(*args):
    """
    Функция принимает произвольное число аргументов и возвращает их mex,
    то есть minimal excluded - минимальное целое неотрицательное число,
    отсутствующее среди них
    """
    count = 0
    while True:
        if count not in args:
            return count


def replace_keys(data: dict[str, Any], **kwargs: str):
    """
    Функция принимает словарь со строковыми ключами и набор аргументов вида
    key=value, и возвращает копию этого словаря, в котором каждый ключ key
    переименован в соответствующий ему value
    """
    res = {}
    for i in data:
        if i in kwargs.keys():
            res[kwargs[i]] = data[i]
        else:
            res[i] = data[i]

    return res


# HIGH ORDER

def count_calls_until(f: Callable, start, condition: Callable[..., bool]):
    """
    Функция принимает другую функцию от одного аргумента f, начальное значение
    и условие остановки, и возвращает количество последовательных вызовов f от
    значения start, пока результат не начнет удовлетворять условию остановки
    """
    c = 0
    x = start
    while not condition(x):
        x = f(x)
        c += 1

    return c


def bind(f: Callable, **kwargs):
    """
    Функция принимает другую функцию от произвольного набора аргументов f и
    возвращает новую функцию, вызов которой идентичен вызову f, но с уже
    заранее подставленными указанными в **kwargs аргументами
    """
    return lambda **kwargs1: f(**dict(kwargs, **kwargs1))
