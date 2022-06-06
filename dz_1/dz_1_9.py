# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# Вариант 1
def get_middle_number_1(nums: list) -> int:
    return nums[len(nums) // 2]

# Вариант 2
def get_middle_number_2(a: int, b: int, c: int) -> int:
    if a < b < c or c < b < a:
        return b
    elif b < a < c or c < a < b:
        return a
    return c


if __name__ == '__main__':
    # Вариант 1
    user_input = sorted(list((map(int, input('Введите три числа(через пробел): ').split()))))
    print(get_middle_number_1(user_input))

    # Вариант 2
    first_num = int(input('Введите первое число: '))
    second_num = int(input('Введите второе число: '))
    third_num = int(input('Введите третье число: '))
    print(get_middle_number_2(first_num, second_num, third_num))
