import math
"""
1. В проекте создать новый модуль test_python.py

2. В модуле написать тесты для встроенных функций
filter, map, sorted, а также для функций из библиотеки
math: pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше
"""


def test_filter():
    numbers = [-2, -1, 0, 1, 2]
    positive_numbers = filter(lambda n: n > 0, numbers)
    assert list(positive_numbers) == [1, 2]

def test_map():
    d = {"key1": 10, "key2": 23}
    assert "key1" in d
    assert  list(d.values()) == [10, 23]

def test_sorted():
    l = [7,6,5,4,3,2,1]
    assert sorted(l) == [1,2,3,4,5,6,7]

def test_pi():
    assert math.pi == 3.141592653589793

def test_sqrt():
    assert math.sqrt(9) == 3.0
    assert math.sqrt(4) == 2.0

def test_pow():
    assert pow(2, 2) == 4
    assert pow(2, 3) == 8
    assert pow(4, 3) == 64

def test_hypot():
    assert math.hypot(4, 1) == 4.123105625617661
    assert math.hypot(-2, 0) == 2.0
    assert math.hypot(-1, 2) == 2.23606797749979