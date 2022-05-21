# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

def sum_between_max_min(numbers: list) -> int:
    min_number_index = numbers.index(min(numbers))
    max_number_index = numbers.index(max(numbers))
    return sum(numbers[min_number_index + 1:max_number_index])


if __name__ == '__main__':
    print(sum_between_max_min([1, 2, 3, 4, 5]))
    print(sum_between_max_min([1, 3, 3, 3, 5]))
    print(sum_between_max_min([1, 0, 3, 4, 5]))
