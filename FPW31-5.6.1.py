GField = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
WinComb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

Player_list = (['Player1', '', 'X'], ['Player2', '', 'O'])

for i in Player_list:
    i[1] = input(f'Input {i[0]} name:')

curPlayer = [Player_list[0][1], Player_list[0][2]]


def drw_field(GField):
    print('-' * 13)
    for i in range(3):
        print('|', GField[0 + i * 3], '|', GField[1 + i * 3], '|', GField[2 + i * 3], '|')
        print('-' * 13)


def movepl(curPlayer):
    chk = False
    while not chk:
        plf = input(f'{curPlayer[0].capitalize()}, please select field to place mark:')
        try:
            plf = int(plf)
            if 0 < plf <= 9:
                while GField[(plf - 1)] == 'X' or GField[(plf - 1)] == 'O':
                    plf = int(input('Already used, please select other field:'))
                else:
                    GField[plf - 1] = curPlayer[1]
                    chk = True
            else:
                print('!!!Only number 1-9 permit!!!')
                continue
        except:
            print('!!!Only number 1-9 permit!!!')
            continue


def win_chk(GField):
    for wc in WinComb:
        if GField[wc[0]] == GField[wc[1]] == GField[wc[2]]:
            print(f"Player {curPlayer[0]} Win!!")
            return True
    return False


def main_play_g(GField):
    turn = 0
    endg = False
    while not endg:
        drw_field(GField)
        if win_chk(GField):
            endg = True
            break
        elif turn == 9:
            print('No winner!')
            endg = True
            break
        if turn % 2 == 0:
            curPlayer = [Player_list[0][1], Player_list[0][2]]
        else:
            curPlayer = [Player_list[1][1], Player_list[1][2]]
        movepl(curPlayer)
        turn += 1
    drw_field(GField)


main_play_g(GField)

input('Enter to exit!')
