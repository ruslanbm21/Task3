from random import randint, choice, seed
from decimal import Decimal as De
from tech3 import add, mul, find_min, find_max, read_file_to_arr
from time import time
from os import remove


# Тест "на мое усмотрение" проверяет корректность функции чтения файла в массив
def test_read_file_to_arr():
    seps = [' ', '  ', '   ', '    ', '\n', ' \n']

    with open('test_file5731.txt', 'w') as f:
        seed(42)  # При указанном seed файл содержит все сепараторы из seps
        rand_arr = rand_num_arr(100, -999999999999, 999999999999)

        for n in rand_arr:
            f.write(f'{n}{choice(seps)}')

    arr_read_from_file = read_file_to_arr('test_file5731.txt')

    assert len(arr_read_from_file) == len(rand_arr)

    for i in range(len(arr_read_from_file)):
        assert arr_read_from_file[i] == rand_arr[i]

    remove('test_file5731.txt')


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

    for i in range(1000):
        g = rand_num_arr(100, -99999999, 99999999)
        assert add(g) == sum(g)


def test_find_min():
    seed(42)

    for i in range(1000):
        g = rand_num_arr(100, -99999999, 99999999)
        assert find_min(g) == min(g)


def test_find_max():
    seed(42)

    for i in range(1000):
        g = rand_num_arr(100, -99999999, 99999999)
        assert find_max(g) == max(g)


time_limits = {
    'add': {
        100: 0.00006,
        1000: 0.0006,
        5000: 0.003
        },
    'mul': {
        100: 0.0001,
        1000: 0.001,
        5000: 0.005
        },
    'min': {
        100: 0.0015,
        1000: 0.003,
        5000: 0.015
        },
    'max': {
        100: 0.0015,
        1000: 0.003,
        5000: 0.015
        }
}


def test_time_add():
    res = [0, 0, 0]
    seed(42)

    for i in range(100):
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

    res = list(map(lambda x: x / 100, res))
    assert res[0] < time_limits['add'][100]
    assert res[1] < time_limits['add'][1000]
    assert res[2] < time_limits['add'][5000]


def test_time_mul():
    res = [0, 0, 0]
    seed(42)

    for i in range(100):
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

    res = list(map(lambda x: x / 100, res))
    assert res[0] < time_limits['mul'][100]
    assert res[1] < time_limits['mul'][1000]
    assert res[2] < time_limits['mul'][5000]


def test_time_find_min():
    res = [0, 0, 0]
    seed(42)

    for i in range(100):
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

    res = list(map(lambda x: x / 100, res))
    assert res[0] < time_limits['min'][100]
    assert res[1] < time_limits['min'][1000]
    assert res[2] < time_limits['min'][5000]


def test_time_find_max():
    res = [0, 0, 0]
    seed(42)

    for i in range(100):
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

    res = list(map(lambda x: x / 100, res))
    assert res[0] < time_limits['max'][100]
    assert res[1] < time_limits['max'][1000]
    assert res[2] < time_limits['max'][5000]
