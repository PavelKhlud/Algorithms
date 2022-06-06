# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
import random


def guess_number():
    print('Игра угадай число!')
    counter = 0
    number = random.randint(1, 100)

    while True:
        counter += 1
        if counter > 10:
            print(f'Вы не угадали, загаданное число {number}')
            break
        user_input = int(input('Введите число: '))
        if user_input > number:
            print('Ваше число больше!')
        elif user_input < number:
            print('Ваше число меньше!')


if __name__ == '__main__':
    guess_number()
