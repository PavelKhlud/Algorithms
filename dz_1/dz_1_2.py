# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака. Объяснить полученный результат.

print('-' * 25 + 'Пункт №1' + '-' * 25)
# 1) Побитовое И
print(bin(5), bin(6))
print(bin(5 & 6))
# Применяет логический оператор И к битовому представлению числа (1 & 1 == 1, 0 & 0 == 0, 1 & 0 == 0), сравнивая
# каждый элемент

print('-' * 25 + 'Пункт №2' + '-' * 25)

# 2) Побитовое ИЛИ
print(bin(5), bin(6))
print(bin(5 | 6))
# Применяет логический оператор ИЛИ к битовому представлению числа (1 & 1 == 1, 0 & 0 == 0, 1 & 0 == 1), сравнивая
# каждый элемент

print('-' * 25 + 'Пункт №3' + '-' * 25)

# 3) Побитовый сдвиг вправо
print(bin(5))
print(bin(5 >> 2))
print(5 >> 2)
# Значение левого операнда будет перемещено вправо на количество бит, заданное правым операндом, эквивалентно 5 / 2 ** 2
# Два числа в конце битового представления были отброшены

print('-' * 25 + 'Пункт №4' + '-' * 25)

# 3) Побитовый сдвиг влево
print(bin(5))
print(bin(5 << 2))
print(5 << 2)
# Значение левого операнда будет перемещено влево на количество бит, заданное правым операндом, эквивалентно 5 * 2 ** 2
# В результате сдвига в конец битового представления были добавлены два нуля
