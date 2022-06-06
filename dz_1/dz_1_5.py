from string import ascii_lowercase


# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
def get_distance_between_two_letters(start_letter: str, end_letter: str) -> str:
    first_letter_index = ascii_lowercase.index(start_letter)
    second_letter_index = ascii_lowercase.index(end_letter)
    return f'Порядковый номер первой буквы - {first_letter_index + 1}, второй - {second_letter_index + 1}, ' \
           f'букв между ними {second_letter_index - first_letter_index}.'


if __name__ == '__main__':
    print(get_distance_between_two_letters(input('Введите первую букву: '),
                                           input('Введите вторую букву: ')))
