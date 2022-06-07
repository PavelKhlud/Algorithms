import random


# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).


def bubble_sort(list):
    print(f'До сортировки: {list}')

    for i in range(len(list) - 1):
        flag = False
        for j in range(len(list) - i - 1):
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                flag = True

        if not flag:
            break

    return list


if __name__ == '__main__':
    print(f'Список после сортировки: {bubble_sort([random.randrange(-100, 100) for _ in range(10)])}')
    print('-' * 72)
    print(f'Список после сортировки: {bubble_sort([-4, -3, -2, -1, 0, 1, 2, 3, 4])}')
