from random import randint, seed
from decimal import Decimal as De
from tech3 import add, mul, find_min, find_max
from time import time
from datetime import datetime


# Тест "на моё усмотрение" проверяет, что тестирование происходит не во время, отведённое на здоровый сон
def test_correct_time_to_test():
    assert 6 < int(str(datetime.now()).split()[1].split(':')[0]) < 23


def rand_num_arr(length, low, high):
    res = []
    for i in range(length):
        res.append(De(str(randint(low, high)) + '.' + str(randint(0, 999999999))))
    return res


def test_mul():
    assert mul([De(str(10 ** 1000000))]) == De('Inf')
    assert mul([De(str(-3)), De(str(7.5)), De(str(11)), De(str(14)), De(str(2.127)), De(str(0.64))]) == De('-4716.8352')
    assert mul([De(str(5)), De(str(-5)), De(str(0)), De(str(0.4))]) == De('0')
    assert mul([De(str(5 ** 10)), De(str(10 ** 10)), De(str(3 ** 5)), De(str(0.8)) ** 5]) == De('7776000000000000000')


def test_add():
    seed(42)

    for i in range(10000):
        g = rand_num_arr(100, -99999999, 99999999)
        assert add(g) == sum(g)


def test_find_min():
    seed(42)

    for i in range(10000):
        g = rand_num_arr(100, -99999999, 99999999)
        assert find_min(g) == min(g)


def test_find_max():
    seed(42)

    for i in range(10000):
        g = rand_num_arr(100, -99999999, 99999999)
        assert find_max(g) == max(g)


time_limits = {
    'add': {
        100: 0.000027,
        1000: 0.00018,
        5000: 0.0009
        },
    'mul': {
        100: 0.00003,
        1000: 0.0003,
        5000: 0.0015
        },
    'fmin': {
        100: 0.000015,
        1000: 0.00007,
        5000: 0.00035
        },
    'fmax': {
        100: 0.000015,
        1000: 0.00007,
        5000: 0.00035
        }
}


def test_time_add():
    res = [0, 0, 0]
    seed(42)

    for i in range(1000):
        g = rand_num_arr(100, -99999999999, 99999999999)
        start = time()
        add(g)
        res[0] += time() - start

        g = rand_num_arr(1000, -99999999999, 99999999999)
        start = time()
        add(g)
        res[1] += time() - start

        g = rand_num_arr(5000, -99999999999, 99999999999)
        start = time()
        add(g)
        res[2] += time() - start

    res = list(map(lambda x: x / 1000, res))
    assert res[0] < time_limits['add'][100]
    assert res[1] < time_limits['add'][1000]
    assert res[2] < time_limits['add'][5000]


def test_time_mul():
    res = [0, 0, 0]
    seed(42)

    for i in range(1000):
        g = rand_num_arr(100, -99999999999, 99999999999)
        start = time()
        mul(g)
        res[0] += time() - start

        g = rand_num_arr(1000, -99999999999, 99999999999)
        start = time()
        mul(g)
        res[1] += time() - start

        g = rand_num_arr(5000, -99999999999, 99999999999)
        start = time()
        mul(g)
        res[2] += time() - start

    res = list(map(lambda x: x / 1000, res))
    assert res[0] < time_limits['mul'][100]
    assert res[1] < time_limits['mul'][1000]
    assert res[2] < time_limits['mul'][5000]


def test_time_find_min():
    res = [0, 0, 0]
    seed(42)

    for i in range(1000):
        g = rand_num_arr(100, -99999999999, 99999999999)
        start = time()
        find_min(g)
        res[0] += time() - start

        g = rand_num_arr(1000, -99999999999, 99999999999)
        start = time()
        find_min(g)
        res[1] += time() - start

        g = rand_num_arr(5000, -99999999999, 99999999999)
        start = time()
        find_min(g)
        res[2] += time() - start

    res = list(map(lambda x: x / 1000, res))
    assert res[0] < time_limits['fmin'][100]
    assert res[1] < time_limits['fmin'][1000]
    assert res[2] < time_limits['fmin'][5000]


def test_time_find_max():
    res = [0, 0, 0]
    seed(42)

    for i in range(1000):
        g = rand_num_arr(100, -99999999999, 99999999999)
        start = time()
        find_max(g)
        res[0] += time() - start

        g = rand_num_arr(1000, -99999999999, 99999999999)
        start = time()
        find_max(g)
        res[1] += time() - start

        g = rand_num_arr(5000, -99999999999, 99999999999)
        start = time()
        find_max(g)
        res[2] += time() - start

    res = list(map(lambda x: x / 1000, res))
    assert res[0] < time_limits['fmax'][100]
    assert res[1] < time_limits['fmax'][1000]
    assert res[2] < time_limits['fmax'][5000]
