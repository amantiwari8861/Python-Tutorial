from time import sleep
import random

def dupli_remover(list):
    l1 = []
    for i in list:
        if i not in l1:
            l1.append(i)
    return l1


def obj_inverter(obj):
    if obj == 'o':
        obje = 'x'
    elif obj == 'x':
        obje = 'o'
    return obje


def move_maker(matrix, posi, obj):
    temprory_matrix = []
    for i in range(len(matrix)):
        new = ''
        for j in matrix[i]:
            if j == str(posi):
                new += obj
            else:
                new += j
        temprory_matrix.append(new)
    return temprory_matrix


def unoccupied(matrix):
    available_places = []
    for i in range(3):
        for j in matrix[i]:
            if j == 'o' or j == 'x':
                continue
            else:
                available_places.append(int(j))
    return available_places


def test1(matrix, obj):
    s1 = [False,]
    for i in matrix:
        if i.count(obj) == 2 and i.count(obj_inverter(obj)) == 0:
            s1[0] = True
            for j in i:
                if j in '123456789':
                    s1.append(j)
    s1 = list(dict.fromkeys(s1))
    return s1


def test2(matrix, obj):
    bi_obj = obj_inverter(obj)
    s2 = [False,]
    for i in matrix:
        if i.count(bi_obj) == 2 and i.count(obj) == 0:
            s2[0] = True
            for j in i:
                if j in '123456789':
                    s2.append(j)
    s2 = list(dict.fromkeys(s2))
    return s2


def test3(matrix, obj):
    s3 = [False,]
    available = unoccupied(matrix)
    for i in available:
        temprory_matrix = move_maker(matrix, i, obj)
        s1 = test1(temprory_matrix, obj)
        if s1[0] == True and len(s1) >= 3:
            s3[0] = True
            s3.append(str(i))
    s3 = list(dict.fromkeys(s3))
    return s3


def test4(matrix, obj):
    bi_obj = obj_inverter(obj)
    s4 = [False,]
    available = unoccupied(matrix)
    for i in available:
        temp_matrix = move_maker(matrix, i, obj)
        s2 = test2(temp_matrix, bi_obj)
        if s2[0] == True:
            temp_matrix_2 = move_maker(temp_matrix, int(s2[1]), bi_obj)
            s2 = test2(temp_matrix_2, obj)
            s3 = test3(temp_matrix_2, obj)
            if s3[0] == True and s2[0] == False:
                s4[0] = True
                s4.append(str(i))
            elif s3[0] == True and s2[0] == True:
                if s2[1] in s3:
                    s4[0] = True
                    s4.append(str(i))
    s4 = list(dict.fromkeys(s4))
    return s4


def test5(matrix, obj):
    bi_obj = obj_inverter(obj)
    s5 = [False,]
    available = unoccupied(matrix)
    for i in available:
        temp_matrix = move_maker(matrix, i, obj)
        s1 = test1(temp_matrix, bi_obj)
        s3 = test3(temp_matrix, bi_obj)
        s4 = test4(temp_matrix, bi_obj)
        if s4[0] == False and s3[0] == False and s1[0] == False:
            s5[0] = True
            s5.append(str(i))

    s5 = list(dict.fromkeys(s5))
    return s5


def test6(matrix, obj):
    bi_obj = obj_inverter(obj)
    s6 = [False,]
    available = unoccupied(matrix)
    for i in available:
        temp_matrix = move_maker(matrix, i, obj)
        s2 = test2(temp_matrix, bi_obj)
        s3 = test3(temp_matrix, bi_obj)
        if s3[0] == False or (s3[0] == True and s2[0] == True and s2[1] != s3[1]):
            s6[0] = True
            s6.append(str(i))

    s6 = list(dict.fromkeys(s6))
    return s6

# ------------------------------------------------------------------------------------------------------------


def game_reader(v_n):
    the_matrix = ['123', '456', '789', '147', '258', '369', '159', '357']
    for i in v_n:
        val = v_n[i]
        if val != ' ' and val != '':
            the_matrix = move_maker(the_matrix, i, val)
    return the_matrix


def move_maker_2(v_n, values):
    matrix = game_reader(v_n)
    s1 = test1(matrix, values[0])
    s2 = test2(matrix, values[0])
    s3 = test3(matrix, values[0])
    s4 = test4(matrix, values[0])
    s5 = test5(matrix, values[0])
    s6 = test6(matrix, values[0])
    if s1[0] == True:
        move = random.choice(s1[1::])
    elif s2[0] == True:
        move = random.choice(s2[1::])
    elif s3[0] == True:
        move = random.choice(s3[1::])
    elif s4[0] == True:
        move = random.choice(s4[1::])
    elif s5[0] == True:
        move = random.choice(s5[1::])
    elif s6[0] == True:
        move = random.choice(s6[1::])
    else:
        move = random.choice(unoccupied(matrix))

    return int(move)

# ============================================================================================================================


def criss_cross(dict1):
    for i in dict1:
        val = dict1[i]
        if val == 'o' or val == 'x':
            continue
        else:
            dict1[i] = ' '
    print("         |         |         ")
    print(f"   {dict1[1]}     |    {dict1[2]}    |    {dict1[3]}    ")
    print("         |         |         ")
    print("_ _ _ _ _|_ _ _ _ _|_ _ _ _")
    print("         |         |         ")
    print(f"   {dict1[4]}     |    {dict1[5]}    |    {dict1[6]}    ")
    print("         |         |         ")
    print("_ _ _ _ _|_ _ _ _ _|_ _ _ _")
    print("         |         |         ")
    print(f"   {dict1[7]}     |    {dict1[8]}    |    {dict1[9]}    ")
    print("         |         |         ")


def pvp_game():
    v_n = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',
           6: ' ', 7: ' ', 8: ' ', 9: ' '}  # value noter
    global values
    in_process = True
    while in_process:
        if v_n[1] == v_n[2] == v_n[3] != ' ' or v_n[4] == v_n[5] == v_n[6] != ' ' or v_n[7] == v_n[8] == v_n[9] != ' ':
            score_updater(values[1])
            print(f"{values[1]} wins")
            in_process = False
        elif v_n[1] == v_n[4] == v_n[7] != ' ' or v_n[2] == v_n[5] == v_n[8] != ' ' or v_n[3] == v_n[6] == v_n[9] != ' ':
            print(f"{values[1]} wins")
            score_updater(values[1])
            in_process = False
        elif v_n[1] == v_n[5] == v_n[9] != ' ' or v_n[3] == v_n[5] == v_n[7] != ' ':
            print(f"{values[1]} wins")
            score_updater(values[1])
            in_process = False
        elif ' ' not in list(v_n.values()):
            print("Draw")
            in_process = False
        else:
            print((f"{namefier(values[0])}'s turn"))
            wrong_input = False
            place = input("Enter the position: ")
            try:
                int(place)
            except:
                wrong_input = True
            if wrong_input == False and int(place) in range(0, 10):
                place = int(place)
                if v_n[place] != ' ':
                    print("Wrong input.Place already occupied.")
                elif values[0] == 'o':
                    v_n[place] = 'o'
                    values = values[::-1]
                elif values[0] == 'x':
                    v_n[place] = 'x'
                    values = values[::-1]
                else:
                    print("some error has occured")
            else:
                print("wrong input")
            criss_cross(v_n)
    score_board(0)
    return True


def p_vs_bot_game():
    v_n = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',
           6: ' ', 7: ' ', 8: ' ', 9: ' '}  # value noter
    global values
    in_process = True
    while in_process:
        if v_n[1] == v_n[2] == v_n[3] != ' ' or v_n[4] == v_n[5] == v_n[6] != ' ' or v_n[7] == v_n[8] == v_n[9] != ' ':
            score_updater(values[1])
            print(f"{values[1]} wins")
            in_process = False
        elif v_n[1] == v_n[4] == v_n[7] != ' ' or v_n[2] == v_n[5] == v_n[8] != ' ' or v_n[3] == v_n[6] == v_n[9] != ' ':
            print(f"{values[1]} wins")
            score_updater(values[1])
            in_process = False
        elif v_n[1] == v_n[5] == v_n[9] != ' ' or v_n[3] == v_n[5] == v_n[7] != ' ':
            print(f"{values[1]} wins")
            score_updater(values[1])
            in_process = False
        elif ' ' not in list(v_n.values()):
            print("Draw")
            in_process = False
        else:
            if values[0] == 'o':
                print((f"{namefier(values[0])}'s turn"))
                wrong_input = False
                place = input("Enter the position: ")
                try:
                    int(place)
                except:
                    wrong_input = True
                if wrong_input == False and int(place) in range(0, 10):
                    place = int(place)
                    if v_n[place] != ' ':
                        print("Wrong input.Place already occupied.")
                    elif values[0] == 'o':
                        v_n[place] = values[0]
                        values = values[::-1]
                    else:
                        print("some error has occured")
                else:
                    print("wrong input")
            else:
                print((f"{namefier(values[0])}'s turn"))
                print((f"{namefier(values[0])} is thinking..."))
                sleep(3)
                v_n[move_maker_2(v_n, values)] = values[0]
                values = values[::-1]
            criss_cross(v_n)
    score_board(0)
    return True


def score_board(fn=0):
    global info_chart
    global values
    if fn == 0:
        print(info_chart[0], "[o]: ", info_chart[2])
        print(info_chart[1], "[x]: ", info_chart[3])
    elif fn == 1:
        player1 = input("Enter player 1 name: ")
        info_chart[0] = player1
    elif fn == 2:
        if _state == 2 or _state == 3:
            player2 = random.choice(
                ['Spencer', 'V-TTT', 'Ash', 'PRC', 'Vidit'])
        else:
            player2 = input("Enter player 2 name: ")
        info_chart[1] = player2
    elif fn == 3:
        info_chart[2] += 1
    elif fn == 4:
        info_chart[3] += 1
    elif fn == 5:
        info_chart = ["Player1", 'Player2', 0, 0]
        values = ['o', 'x']


def state(st=0):
    global _state
    if st == 0:
        _state = 0  # New game (just strted)
    elif st == 1:
        _state = 1  # continue game
    elif st == 2:
        _state = 2  # pvbot
    elif st == 3:
        _state = 3  # rvbot continue game
    else:
        _state = 4  # End


def score_updater(wi):
    if wi == 'o':
        score_board(3)
    elif wi == 'x':
        score_board(4)
    else:
        return


def namefier(wi):
    if wi == 'o':
        return info_chart[0]
    elif wi == 'x':
        return info_chart[1]
    else:
        return


values = ['o', 'x']
# player1_name , player_2 name , player1 score , player 2 score
info_chart = ["Player1", 'Player2', 0, 0]


# -----------------------------------------------------------------------------------------------------------------#

_state = 0
print("----WELCOME TO TIC TAC TOE GAME----")
print("Credits - Chirag Sugla")
mod = True
while mod:
    print(
        "Enter \n [0] to exit \n [1] to start for 2 players \n [2] to start player vs bot")
    _start = input(": ")
    if _start == '0':
        mod = False
        state(4)
    elif _start == '2':
        state(2)
        mod2 = True
        while mod2:
            if _state == 2:
                print("Enter \n [0] to exit \n [1] to start new game ")
                _play = input(": ")
                if _play == '0':
                    mod2 = False
                    score_board(0)
                elif _play == '1':
                    score_board(1)
                    score_board(2)
                    p_vs_bot_game()
                    state(3)
            elif _state == 3:
                print(
                    "Enter \n [0] to exit \n [1] to continue \n [2] to start new game \n [3] to change player name")
                _play = input(": ")
                if _play == '0':
                    mod2 = False
                elif _play == '1':
                    p_vs_bot_game()
                    state(3)
                elif _play == '2':
                    score_board(5)
                    score_board(1)
                    score_board(2)
                    pvp_game()
                elif _play == '3':
                    score_board(1)
                    print("Score Board updated successfully :)")
                else:
                    print("Wrong input")
            else:
                continue
    elif _start == '1':
        state(0)
        mod2 = True
        while mod2:
            if _state == 0:
                print("Enter \n [0] to exit \n [1] to start new game ")
                _play = input(": ")
                if _play == '0':
                    mod2 = False
                elif _play == '1':
                    score_board(1)
                    score_board(2)
                    pvp_game()
                    state(1)
            elif _state == 1:
                print(
                    "Enter \n [0] to exit \n [1] to continue \n [2] to start new game \n [3] to change player name")
                _play = input(": ")
                if _play == '0':
                    mod2 = False
                elif _play == '1':
                    pvp_game()
                    state(1)
                elif _play == '2':
                    score_board(5)
                    score_board(1)
                    score_board(2)
                    pvp_game()
                elif _play == '3':
                    score_board(1)
                    score_board(2)
                    print("Score Board updated successfully :)")
                else:
                    print("Wrong input")
            else:
                continue
else:
    print("Thanks for playing.")