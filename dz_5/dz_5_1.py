# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.

def enterprise_stat():
    enterprises = dict()
    amount = int(input('Введите количество предприятий: '))

    for i in range(1, amount + 1):
        name = input(f'Введите название {i} предприятия: ')
        enterprises[name] = []
        for j in range(1, 5):
            income = int(input(f'Введите прибыль за {j} квартал: '))
            enterprises[name].append(income)

    avg_income = sum(map(sum, enterprises.values())) / len(enterprises.values())

    print(f'Средняя прибыль: {avg_income}')

    print('Компании с прибылью меньше среднего:')
    for company, income in enterprises.items():
        if sum(income) < avg_income:
            print(company)

    print('Компании с прибылью больше среднего:')
    for company, income in enterprises.items():
        if sum(income) > avg_income:
            print(company)


enterprise_stat()

# Сложность O(n^2)
