# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке[0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge(list_1, list_2):
    i = 0
    j = 0
    result_lst = []
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result_lst.append(list_1[i])
            i += 1
        else:
            result_lst.append(list_2[j])
            j += 1
    result_lst += list_1[i:] + list_2[j:]
    return result_lst


def merge_sort(lst):
    N = len(lst) // 2
    first_part = lst[:N]
    second_part = lst[N:]

    if len(first_part) > 1:
        first_part = merge_sort(first_part)
    if len(second_part) > 1:
        second_part = merge_sort(second_part)

    return merge(first_part, second_part)


if __name__ == '__main__':
    print(merge_sort([random.uniform(0, 50) for _ in range(10)]))
    print(merge_sort([2, 5, 6, 7, 8, 9, 1, 3, 4, 11, 16, 22, 3]))
