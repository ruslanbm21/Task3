from decimal import Decimal
import decimal


def read_file_to_arr(_filename):
    res = []
    with open(_filename) as f:
        for line in f:
            for n in line.split():
                res.append(Decimal(n))
    return res


def add(numbers_arr):
    res = Decimal('0')
    for n in numbers_arr:
        try:
            res += n
        except decimal.Overflow:
            return Decimal('Inf')
    return res


def mul(numbers_arr):
    res = Decimal('1')
    for n in numbers_arr:
        try:
            res *= n
        except decimal.Overflow:
            return Decimal('Inf')
    return res


def find_min(numbers_arr):
    res = numbers_arr[0]
    for n in numbers_arr:
        if n < res:
            res = n
    return res


def find_max(numbers_arr):
    res = numbers_arr[0]
    for n in numbers_arr:
        if n > res:
            res = n
    return res
