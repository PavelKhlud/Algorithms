# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y=kx+b, проходящей через эти точки.
x1, y1 = map(float, input('Введите координаты первой точки(через пробел): ').split(' '))
x2, y2 = map(float, input('Введите координаты второй точки(через пробел): ').split(' '))
if x1 != x2:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - (y1 - y2) / (x1 - x2) * x2
    print(f'Уравнение прямой y = {k}x + {b}')
else:
    print(f'Уравнение прямой x = {x1}')