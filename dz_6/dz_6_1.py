from functools import reduce
from sys import getsizeof

# Система Mac OS X Monterey
# 64bit
# python - 3.10.4


# 1) вариант
def sum_and_multiplication_of_user_num_1(user_input: str) -> str:
    # Переменная user_input занимает 52 байта - 49 байт строк + 3 байта символы
    user_input_lst = [int(item) for item in user_input]
    print(getsizeof(user_input_lst))
    # Размер списка: 88 байт = 56(место занимаемое списком) + 32 байта
    # Не особо понимаю почему, ведь он должен занимать 80 (56 + 8 + 8 + 8)
    # Обьясните пожалуйста)
    print(user_input_lst)
    return f'Сумма - {sum(user_input_lst)}, произведение - {reduce(lambda x, y: x * y, user_input_lst)}'


# 2) вариант
def sum_and_multiplication_of_user_num_2(num: str):
    # Переменная user_input занимает 52 байта - 49 байт строк + 3 байта символы
    num_sum = '+'.join(list(num))  # размер строки 54 байта: 49 - пустая строка + 5 на знаки (+ повторяется дважды)
    num_mult = '*'.join(list(num))  # размер строки 54 байта: 49 - пустая строка + 5 на знаки (+ повторяется дважды)
    return f'Сумма - {eval(num_sum)}, произведение - {eval(num_mult)}'


if __name__ == '__main__':
    # Вывод 1-го варианта
    print(sum_and_multiplication_of_user_num_1(
        (input("Введите трехзначное число: ")))
    )

    # Вывод 2-го варианта
    print(sum_and_multiplication_of_user_num_2(
        input("Введите трехзначное число: "))
    )
