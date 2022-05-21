# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
def swap_max_min_numbers(numbers: list) -> list:
    max_number_index = numbers.index(max(numbers))
    min_number_index = numbers.index(min(numbers))
    numbers[min_number_index], numbers[max_number_index] = numbers[max_number_index], numbers[min_number_index]
    return numbers


if __name__ == '__main__':
    print(swap_max_min_numbers([1, 2, 3, 4, 5, 6]))
    print(swap_max_min_numbers([0, 1, 2, 99, 68]))
    print(swap_max_min_numbers([10, 9, 8, 7, 6, 5]))
