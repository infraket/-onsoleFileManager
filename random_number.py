import random


def game_number():
    number = random.randint(1, 100)
    while True:
        user_number = int(input('Введите число : '))
        if number == user_number:
            print('Победа')
            break
        elif number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')


if __name__ == '__main__':
    game_number()
