# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

def two_minimal_nmbers(numbers: list) -> str:
    numbers = set(numbers)
    min1, min2 = sorted(numbers)[0: 2]
    return f'Два минимальных числа {min1} и {min2}'


if __name__ == '__main__':
    print(two_minimal_nmbers([1, 2, 3, 4, 5, 0]))
    print(two_minimal_nmbers([0, 0, 0, 1, 2, -1]))
    print(two_minimal_nmbers([3, 4, 5, 6, 7, 8]))
