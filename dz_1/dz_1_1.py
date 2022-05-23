from functools import reduce


# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# 1) вариант
def sum_and_multiplication_of_user_num_1(user_input: str) -> str:
    user_input_lst = [int(item) for item in user_input]
    return f'Сумма - {sum(user_input_lst)}, произведение - {reduce(lambda x, y: x * y, user_input_lst)}'


# 2) вариант
def sum_and_multiplication_of_user_num_2(num: str):
    num_sum = '+'.join(list(num))
    num_mult = '*'.join(list(num))
    print(f'Сумма - {eval(num_sum)}, произведение - {eval(num_mult)}')


if __name__ == '__main__':
    # Вывод 1-го варианта
    print(sum_and_multiplication_of_user_num_1(
        (input("Введите трехзначное число: ")))
    )

    # Вывод 2-го варианта
    print(sum_and_multiplication_of_user_num_2(
        input("Введите трехзначное число: "))
    )
