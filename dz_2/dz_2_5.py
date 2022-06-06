# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.

for i, num in enumerate(range(32, 128)):
    if i % 10 == 9:
        delimiter = '\n'
    else:
        delimiter = ' '

    print(f'{num}:{chr(num)}', end=delimiter)
