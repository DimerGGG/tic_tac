v = 0.18

import os
from random import randrange

cell = {i: str(i) for i in range(1, 10)}

who_next2 = None
winner = None
randome = randrange(100)
status = None

def greating():
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
          "            #########################\n"
          "\n"
          "\n"
          "Version", v)
    input("\n\nНажмите любую клавишу для продолжения...")
    os.system('cls')

def draw_field():
    os.system('cls')
    field = "\n".join([f"            | {cell[i]} | {cell[i+1]} | {cell[i+2]} |\n            ------------- " for i in range(1, 10, 3)])
    print(field)

def update_cell_value():
    global who_next2
    draw_field()
    if who_next2 == 'x':
        print("Ход Игрок_1 - X")
    elif who_next2 == 'o':
        print("Ход Игрок_2 - O")
    try:
        position = int(input("Введите номер ячейки для изменения (1-9): "))
    except ValueError:
        print("Пожалуйста, введите число от 1 до 9.")
        update_cell_value()
        return
    if position in cell:
        if cell[position] == 'x' or cell[position] == 'o':
            print("Эта ячейка уже занята. Выберите другую ячейку.")
            update_cell_value()
        else:
            cell[position] = who_next2 or 'x'
            if who_next2 == 'x':
                who_next2 = 'o'
            elif who_next2 == 'o':
                who_next2 = 'x'
            return
    else:
        print("Неверный номер ячейки. Пожалуйста, введите число от 1 до 9.")
        update_cell_value()

def check_for_stop():
    global status
    if winner == "x":
        print("\nПобедил Игрок_1!\n")
        status = 'stop'
    elif winner == "o":
        print("\nПобедил Игрок_2!\n")
        status = 'stop'
    elif (cell[1] != '1' and
          cell[2] != '2' and
          cell[3] != '3' and
          cell[4] != '4' and
          cell[5] != '5' and
          cell[6] != '6' and
          cell[7] != '7' and
          cell[8] != '8' and
          cell[9] != '9'):
        status = 'stop'
        print("\nПобедила дружба")

def check_for_win(cell):
    global winner
    if (cell[1] == cell[2] == cell[3]):
        winner = cell[1]
        return True
    elif (cell[4] == cell[5] == cell[6]):
        winner = cell[4]
        return True
    elif (cell[7] == cell[8] == cell[9]):
        winner = cell[7]
        return True
    elif (cell[1] == cell[4] == cell[7]):
        winner = cell[1]
        return True
    elif (cell[2] == cell[5] == cell[8]):
        winner = cell[2]
        return True
    elif (cell[3] == cell[6] == cell[9]):
        winner = cell[3]
        return True
    elif (cell[1] == cell[5] == cell[9]):
        winner = cell[1]
        return True
    elif (cell[3] == cell[5] == cell[7]):
        winner = cell[3]
        return True
    else:
        return False

def first_step():
    global status
    global randome
    global who_next2
    status = 'game'
    print("Игрок1 ходит ноликами - X\n"
          "Игрок2 ходит крестиками - O \n\n")
    input("\n\nНажмите любую клавишу для продолжения...")
    if randome % 2 == 0:
        who_next2 = 'o'
        print(randrange(100), "Первый ход за Игроком2\n")
        draw_field()
        input("\n\nНажмите любую клавишу для продолжения...")
    elif randome % 2 != 0:
        who_next2 = 'x'
        print(randrange(100), "Первый ход за Игроком1\n")
        draw_field()
        input("\n\nНажмите любую клавишу для продолжения...")

greating()
first_step()

while status != 'stop':
    os.system('cls')
    draw_field()
    update_cell_value()
    check_for_win(cell)
    check_for_stop()
