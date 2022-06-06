# 4. Определить, какое число в массиве встречается чаще всего.
from collections import Counter


def max_repeted(numbers: list) -> int:
    numbers_dct = Counter(numbers)
    result = sorted(numbers_dct, key=lambda x: numbers_dct[x], reverse=True)
    return result[0]


if __name__ == '__main__':
    print(max_repeted([1, 2, 1, 1, 1, 4, 5, 6]))
    print(max_repeted([1, 7, 7, 5, 6, 7, 8, 8]))
    print(max_repeted([1, 2, 2, 2, 2, 2, 2, 2]))
    print(max_repeted([0, 1, 2, 3, 0, 0, 0, 0]))
