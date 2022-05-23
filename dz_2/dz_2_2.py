# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def count_even(number: str) -> str:
    even = sum([1 for num in number if int(num) % 2 == 0])
    odd = len(number) - even

    return f'Количество четных чисел - {even}, нечетных - {odd}'


if __name__ == '__main__':
    print(count_even(input('Введите число: ')))
