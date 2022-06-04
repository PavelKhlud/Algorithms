# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

def sum_or_mul_hex(first_num, second_num: str):
    first_num_lst = first_num.split()
    second_num_lst = second_num.split()

    hex_sum = list(hex(int(first_num, 16) + int(second_num, 16)).lstrip('0x').upper())
    hex_mult = list(hex(int(first_num, 16) * int(second_num, 16)).lstrip('0x').upper())

    print(f'Сумма = {hex_sum}')
    print(f'Произведение = {hex_mult}')


print(sum_or_mul_hex(
    input('Введите первое число: '),
    input('Введите второе число: '),
))

# Асимптотическая сложность O(n)
