# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить
# в виде комментариев в файле с кодом.
from math import sqrt, ceil
import cProfile


# Без использования решета Эратосфена:
def simple_num(n: int) -> int:
    lst = [2]
    counter = 3

    while len(lst) < n:
        flag = False
        for num in range(2, ceil(sqrt(counter)) + 1):
            if counter % num == 0:
                flag = True
                break

        if not flag:
            lst.append(counter)

        counter += 1
    return lst


# С использованием Решета Эратосфена

def eratosthenes_sieve(n: int) -> int:
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n + 1, number):
                numbers[candidate - 2] = 0
    return list(filter(lambda x: x != 0, numbers))[-1]


# В моем алгоритме Вы вводите позицию простого числа и программа возвращает число, стоящее на это позиции,
# а решето Эратосфена рассчитывает простые числа до n (у меня выводит последнее просто число перед n)

cProfile.run('simple_num(100000)')
cProfile.run('eratosthenes_sieve(1299710)')

# У моего алгоритма сложность O(n^2)
# У решета Эратосфен на сколько я понимаю сложность O(n log n)
# НУ и выполняется он соответственно в разы быстрее
