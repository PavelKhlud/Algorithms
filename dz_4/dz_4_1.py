# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трех уроков.


# Пример из домашнего задания № 1, задание 1

def sum_and_multiplication_of_user_num_1(user_input: str) -> str:
    user_input_lst = [int(item) for item in user_input]  # O(n)
    return f'Сумма - {sum(user_input_lst)}, произведение - {reduce(lambda x, y: x * y, user_input_lst)}'
    # У sum тоже O(n)
    # Рискну предположить, что у reduce тоже O(n)
    # Отсюда следует, что сложность данного алгоритма O(n)


# 2) вариант
def sum_and_multiplication_of_user_num_2(num: str):
    num_sum = '+'.join(list(num))  # O(n)
    num_mult = '*'.join(list(num))  # O(n)
    print(f'Сумма - {eval(num_sum)}, произведение - {eval(num_mult)}')
    # Eval в обоих случаях занимает O(1)
    # Но сокорость алгоритма от этого особо не поменяется и будет все так же O(n)
