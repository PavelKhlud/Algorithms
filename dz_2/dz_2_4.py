# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с
# клавиатуры.


def elements_sum(elements: str) -> int:
    return sum([float(el) for el in elements.split()])


if __name__ == '__main__':
    print(elements_sum(input('Введите числа через пробел: ')))
