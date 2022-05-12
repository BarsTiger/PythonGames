# Ghost Game
from random import randint
print('Дом с привидениями')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 3)
    print('Впереди три двери...')
    print('Привидение за одной из них.')
    print('Какую ты откроешь?')
    door = input('1, 2 или 3? ')
    door_num = int(door)
    if door_num > 3 or door_num < 1:
        print('Не обманывай!!!')
    else:
        if door_num == ghost_door:
            print('ПРИВИДЕНИЕ!!!')
            feeling_brave = False
        else:
            print('Привидения нет.')
            print('Ты переходишь в следующую комнату')
            score = score + 1
print('Убегай!')
print('Ты проиграл! Твой счёт', score)