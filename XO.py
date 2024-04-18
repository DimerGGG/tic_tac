## TIC TAC TOE

import os
from random import randrange
import time

cell = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
        6: '6', 7: '7',  8: '8', 9: '9'}

who_next = None
winner = None
first_step = None
step = None
randome = None

def draw_field(cell):
    field = (f"|{cell[1]}|{cell[2]}|{cell[3]}|\n"
             f"|{cell[4]}|{cell[5]}|{cell[6]}|\n"
             f"|{cell[7]}|{cell[8]}|{cell[9]}|")
    print(field)

def update_cell_value():
    os.system('cls')
    draw_field(cell)
    position = int(input("Введите номер ячейки для изменения (1-9): "))
    if position in cell:
        if cell[position] == 'x' or cell[position] == 'o':
            print("Эта ячейка уже занята. Выберите другую ячейку.")
            update_cell_value()
        else:
            cell[position] = 'x'
    else:
        print("Неверный номер ячейки. Пожалуйста, введите число от 1 до 9.")
        update_cell_value()

def check_for_win(cell):
    global winner
    if (cell[1] == cell[2] == cell[3]):
        winner = cell[1]
        return True
    elif (cell[4] == cell[5] == cell[6]):
        winner = cell[2]
        return True
    elif (cell[7] == cell[8] == cell[9]):
        winner = cell[2]
        return True
    elif (cell[1] == cell[4] == cell[7]):
        winner = cell[1]
        return True
    elif (cell[2] == cell[5] == cell[8]):
        winner = cell[2]
        return True
    elif (cell[3] == cell[6] == cell[9]):
        winner = cell[2]
        return True
    elif (cell[1] == cell[5] == cell[9]):
        winner = cell[1]
        return True
    elif (cell[3] == cell[5] == cell[7]):
        winner = cell[3]
        return True
    else: return False

os.system('cls')

print("\n\n\n"
      "            #########################\n"
      "            ##                     ##\n"
      "            ##   КРЕСТИКИ НОЛИКИ   ##\n"
      "            ##                     ##\n"
      "            ##       |x|o|x|       ##\n"
      "            ##       | |x|o|       ##\n"
      "            ##       |o| |x|       ##\n"
      "            ##                     ##\n"
      "            #########################\n")

input("\n\nНажмите любую клавишу для продолжения...")
os.system('cls')
type_game = input("Какой тип игры?\n"
                  "1 - игра с компьютером\n"
                  "2 - игра с человеком\n")

if type_game == "1":
    os.system('cls')
    print("Выбран режим игры с компьютером\n")
    print("компьютер ходит ноликами - o\n"
    "игрок ходит крестиками - x \n"
    "\n")
    if randrange(100) % 2 == 0:
        first_step = "o"
        who_next = 1
        print(randrange(100), "Первый ход за компьютером\n")
        draw_field(cell)
        input("\n\nНажмите любую клавишу для продолжения...")

        randome = randrange(4)
        if randome == 1:
            cell[1] = 'o'

        elif randome == 2:
            cell[3] = 'o'
        elif randome == 3:
            cell[7] = 'o'
        else:
            cell[9] = 'o'



    elif randrange(100) % 2 != 0:
        first_step = "x"
        who_next = 0
        print(randrange(100), "Первый ход за игроком\n")
        draw_field(cell)
        input("\n\nНажмите любую клавишу для продолжения...")

    else: os.system('cls')
