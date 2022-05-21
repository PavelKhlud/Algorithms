# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Я не понял как правильно, поэтому вот

# 1
lst = [i for i in range(2, 100)]
dividers = [i for i in range(2, 10)]

for divider in dividers:
    for i in range(len(lst)):
        if lst[i] % divider != 0:
            lst[i] = 0
    result = len([i for i in lst if i != 0])

print(f'В диапазоне от 2 до 99, чисел кратных всем в диапазоне от 2 до 9: {result}')

print('-' * 90)

# 2
lst = [i for i in range(2, 100)]
dividers = [i for i in range(2, 10)]

for divider in dividers:
    counter = 0
    for i in range(len(lst)):
        if lst[i] % divider == 0:
            counter += 1
    print(f'В диапазоне от 2 до 99, чисел кратных {divider}: {counter}')
