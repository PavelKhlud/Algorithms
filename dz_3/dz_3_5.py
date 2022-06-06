# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


def find_max_neg_number(numbers: list) -> str:
    max_neg = sorted([i for i in numbers if i < 0], reverse=True)
    if max_neg:
        return f'Максимальное отрицательное число {max_neg[0]}, его индекс {numbers.index(max_neg[0])}'
    else:
        return 'Нет отрицательных чисел'


if __name__ == '__main__':
    print(find_max_neg_number([-3, -2, -1, 0, 1, 2, 3]))
    print(find_max_neg_number([0, 0, 0, 0]))
