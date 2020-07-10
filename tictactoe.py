game = ("_________")
game_won = 0
game_draw = 0
game_impossible = 0


def lines():
    line1 = []
    line2 = []
    line3 = []
    for i in range(9):
        if i <= 2:
            line1.append(game[i])
        elif 2 < i <= 5:
            line2.append(game[i])
        elif 5 < i <= 9:
            line3.append(game[i])
    return line1, line2, line3


l1, l2, l3 = lines()
matrix = [l1, l2, l3]


def print_board():
    print(f"\
---------\n\
| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |\n\
| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |\n\
| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |\n\
---------\
    ")


winner = []


def line_win():
    if l1[0] == l1[1] == l1[2]:
        if l1[0] != '_':
            winner.append(l1[0])
    if l2[0] == l2[1] == l2[2]:
        if l2[0] != '_':
            winner.append(l2[0])
    if l3[0] == l3[1] == l3[2]:
        if l3[0] != '_':
            winner.append(l3[0])
    return winner


def column_win():
    if l1[0] == l2[0] == l3[0]:
        if l1[0] != '_':
            winner.append(l1[0])
    if l1[1] == l2[1] == l3[1]:
        if l1[1] != '_':
            winner.append(l1[1])
    if l1[2] == l2[2] == l3[2]:
        if l1[2] != '_':
            winner.append(l1[2])
    return winner


def diagonal_win():
    if l1[0] == l2[1] == l3[2]:
        if l1[0] != '_':
            winner.append(l1[0])
    if l1[2] == l2[1] == l3[0]:
        if l2[1] != '_':
            winner.append(l1[2])
    return winner


def no_chars():
    no_o, no_x, no_1 = 0, 0, 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == "X":
                no_x += 1
            if matrix[i][j] == "O":
                no_o += 1
            if matrix[i][j] == "_":
                no_1 += 1
    return no_1, no_o, no_x


def game_state():
    global game_won, game_draw, game_impossible
    no_1, no_x, no_o, = no_chars()
    diagonal_win()
    line_win()
    column_win()
    if len(winner) == 0 and no_1 == 0:
        game_draw = 1
        print("Draw")
    elif len(winner) == 2 or (abs(no_x - no_o) >= 2):
        game_impossible = 1
        print("Impossible")
    elif len(winner) == 0 and no_1 != 0:
        pass
    elif len(winner) == 1:
        game_won = 1
        print(winner[0] + " wins")


def get_coords():
    coords = input("Enter coordinates\n").split(" ")
    return coords


def check_coords(coord):
    if len(coord) < 2:
        return "You should enter numbers!"
    else:
        x = coord[0]
        y = coord[1]
    if not (x.isdigit() and y.isdigit()):
        return "You should enter numbers!"
    elif not ((0 < int(x) <= 3) and (0 < int(y) <= 3)):
        return "Coordinates should be from 1 to 3!"


def convert_coords(coord):
    col = int(coord[0]) - 1
    row = 3 - int(coord[1])
    return row, col


def get_valid_coords():
    coord = get_coords()
    # print(coord)
    while True:
        if check_coords(coord):
            print(check_coords(coord))
            coord = get_coords()
        else:
            i, j = convert_coords(coord)
            return i, j


def check_move(moves):
    if moves % 2 != 0:
        row, col = get_valid_coords()
        if matrix[row][col] == '_':
            matrix[row][col] = 'X'
            return True
    elif moves % 2 == 0:
        row, col = get_valid_coords()
        if matrix[row][col] == '_':
            matrix[row][col] = 'O'
            return True
    return False


def print_board_moves():
    moves = 0
    while True:
        moves += 1
        if not check_move(moves):
            print("This cell is occupied! Choose another one!")
        else:
            print_board()
            game_state()
            if game_won == 1 or game_draw == 1 or game_impossible == 1:
                exit()
            if moves > 9:
                print("Draw")
                exit()


def main():
    print_board()
    print_board_moves()


main()
