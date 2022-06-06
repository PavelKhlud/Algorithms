# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
def is_high_year(year: int) -> str:
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return 'Високосный'
    return 'Невисокосный'


if __name__ == '__main__':
    print(is_high_year(int(input('Введите год: '))))
