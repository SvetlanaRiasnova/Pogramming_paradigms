# создаем игровую доску
board = list(range(1, 10))

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

# получаем выбор игрока и проверем на повтор или не корректное значение
def take_input(player_token):
    valid = False
    while not valid:
        player_choice = input("Куда походит " + player_token + "? ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_choice <= 9:
            if str(board[player_choice - 1]) not in "XO":
                board[player_choice - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

# проверяем победителя
def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

# запускаем игру
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        tmp = check_win(board)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if counter == 8:
            print("Ничья!")
            break
    draw_board(board)


main(board)

