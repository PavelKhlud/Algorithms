# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.

def count_sum_of_numbers(numbers: str) -> int:
    numbers_dct = {sum([int(i) for i in number]): number for number in numbers.split(' ')}
    max_sum = sorted(numbers_dct.keys(), reverse=True)[0]
    return numbers_dct[max_sum]


if __name__ == '__main__':
    print(count_sum_of_numbers(input('Введите числа(через пробел): ')))
