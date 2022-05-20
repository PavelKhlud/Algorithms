# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def theorem_test(number):
    return sum(range(1, number + 1)) == number * (number + 1) / 2


if __name__ == '__main__':
    print(theorem_test(20))
    print(theorem_test(33))
    print(theorem_test(12))
    print(theorem_test(11))