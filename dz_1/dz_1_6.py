from string import ascii_lowercase


# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def get_letter_by_number(num: int) -> str:
    return f'Под номером {num} находится буква {ascii_lowercase[num - 1]}'


if __name__ == '__main__':
    print(get_letter_by_number(int(input('Введите число(от 1 до 26): '))))
