from random import randint
from time import sleep
from data import *
def fight(current_enemy):
    round = randint(1,2)
    enemy = enemies[current_enemy]
    enemy_hp = enemy[current_enemy] ['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter, чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            enemy_hp -= player['attack']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy['hp']}''')
        print()
        sleep(1)
    else:
        print(f'{enemy["name"]} атакует {player["name"]}')
        player['hp'] -= enemy['attack']
        sleep(1)
        print(f'''{player['name']} - {player['hp']})
    {enemy['name']} - {enemy['hp']}''')
        print()
        sleep(1)
        round += 1
    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')


def training(training_type):
    for i in range(0, 101, 20):
        print(f'Тренировка завершена на {i}%')
        if training_type == '1':
            player['attack'] += 2
            print(f'Атака улучшена {player["attack"]}')
        elif training_type == '2':
            player['armor'] -= .09
            print(f'Броня улучшена {100 - player["armor"] * 100}')


def display_hero():
    print(f'Игрок - {player["name"]}')
    print(f'Атака - {player["attack"]}')
    print(f'Защита - {1 - player["armor"] * 100}')


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Величина атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')


def display_inventory():
    print(f'У меня есть: ')
    for value in player['inventory']:
        potion = input('''Выпить зелье:
                       1 - Да
                       2 - Нет''')
        if potion == '1':
            player['luck'] += 7
            player['inventory'].remove('Зелье удачи')


def shop():
    print(f'Привет, путник.')
    print(f'Деньги: {player["money"]}')
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')
    item = input()
    if item in player ['inventory']:
        print(f'Уже есть')
    elif player['money'] >= items[item]['price']:
        print(f'Купил')
        player['inventory'].append(items[item]["name"])
        player['money'] -= items[item]['price']
    else:
        print('Иди работай')
    print()
    print('Возвращайтесь еще.')
    print()


def earn():
    print(f'Добро пожаловать на завод!')
    result = randint(1,100)
    sleep(1,5)
    print('Ииии...')
    sleep(1,5)
    if result < 67:
        print('+500')
        player['money'] += 500
    else:
        print('-500')
        player['money'] -= 500