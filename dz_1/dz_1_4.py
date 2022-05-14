import random


# 4. Написать программу, которая генерирует в указанных пользователем границах:

# случайное целое число;
# случайное вещественное число;
# случайный символ.

# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный
# символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
# включительно.

def get_rand_int_from_interval(start: int, end: int) -> int:
    return random.randint(start, end)


def get_rand_float_from_interval(start: int, end: int) -> float:
    return random.uniform(start, end)


def get_rand_letter_from_interval(start: str, end: str) -> str:
    return chr(random.randint(ord(start), ord(end)))


if __name__ == '__main__':
    user_input_1, user_input_2 = map(int, input('Введите начало и конец диапазона(числа, через пробел): ').split())
    print(get_rand_int_from_interval(user_input_1, user_input_2))
    user_input_3, user_input_4 = map(int, input('Введите начало и конец диапазона(числа, через пробел): ').split())
    print(get_rand_float_from_interval(user_input_3, user_input_4))
    user_input_5, user_input_6 = input('Введите начало и конец диапазона(буквы, через пробел): ').split()
    print(get_rand_letter_from_interval(user_input_5, user_input_6))
