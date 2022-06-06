# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или
# равносторонним.

# Первый вариант
def get_triangle_type_by_sides_length_1(side_1: int, side_2: int, side_3: int) -> str:
    if side_1 + side_2 <= side_3 or side_1 + side_3 <= side_2 or side_2 + side_3 <= side_1:
        return 'Треугольника не существует'
    elif side_1 == side_2 == side_3:
        return 'Треугольника равносторонний'
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        return 'Треугольник равнобедренный'
    return 'Треугольник разносторонний'


# Второй вариант
def get_triangle_type_by_sides_length_2(sides: list) -> str:
    if sides[-1] >= sum(sides[0:-1]):
        return 'Треугольника не существует'
    elif sides.count(sides[0]) == 3:
        return 'Треугольник равносторонний'
    elif sides.count(sides[0]) == 2 or sides.count(sides[1]) == 2:
        return 'Треугольник равнобедренный'
    return 'Треугольник разносторонний'


if __name__ == '__main__':
    # Вывод первого варианта
    print(get_triangle_type_by_sides_length_1(
        int(input('Введите первую сторону треугольника: ')),
        int(input('Введите вторую сторону треугольника: ')),
        int(input('Введите третью сторону треугольника: '))
    ))

    # Вывод второго варианта
    sides_list = sorted(list(map(int, input('Введите стороны треугольника через пробел: ').split())))
    print(get_triangle_type_by_sides_length_2(sides_list))
