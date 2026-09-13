from random import randrange
EMPTY = "-"
 
 
def display_board(board):
    border_line = "+-------+-------+-------+"
    spacer_line = "|       |       |       |"
    print(border_line)
    for row in range(len(board)):
        row_line = f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |"
        print(spacer_line)
        print(row_line)
        print(spacer_line)
        print(border_line)
 
 
def enter_move(board):
    player_choice = int(input("Show me your next move: "))
    if player_choice > 9 or player_choice < 1:
        print("This value is not choosable")
        return enter_move(board)
    elif board[(player_choice-1)//3][(player_choice -1) % 3] == 'X' or board[(player_choice-1)//3][(player_choice -1) % 3] == 'O':
        print("You cant choose this value")
        return enter_move(board)
    else:
        board[(player_choice-1)//3][(player_choice -1) % 3] = 'O'
        return board
 
 
def make_list_of_free_fields(board):
    open_spots = []
    for i in range (9):
        if board[(i)//3][(i) % 3] == EMPTY:
            open_spots.append(((i)//3,(i) % 3))
    return open_spots
 
 
 
def victory_for(board, sign):
    winning_lines = [
    [(0,0),(0,1),(0,2)],   # row 0
    [(1,0),(1,1),(1,2)],   # row 1
    [(2,0),(2,1),(2,2)],   # row 2
    [(0,0),(1,0),(2,0)],   # column 0
    [(0,1),(1,1),(2,1)],   # column 1
    [(0,2),(1,2),(2,2)],   # column 2
    [(0,0),(1,1),(2,2)],   # diagonal
    [(0,2),(1,1),(2,0)],   # diagonal
]
    for line in winning_lines:
        hits = 0
        for cell in line:
            if board[cell[0]][cell[1]] == sign:
                hits = hits + 1
        if hits == 3:
            return True
    return False
 
 
def draw_move(board):
    open_spots = make_list_of_free_fields(board)
    for spot in open_spots:
        board[spot[0]][spot[1]] = 'X'
        if victory_for(board, 'X'):
            return board
        else:
            board[spot[0]][spot[1]] = EMPTY
 
    for spot in open_spots:
        board[spot[0]][spot[1]] = 'O'
        if victory_for(board, 'O'):
            board[spot[0]][spot[1]] = 'X'
            return board
        else:
            board[spot[0]][spot[1]] = EMPTY
    computer_choice =(randrange(len(open_spots)))
    board[open_spots[computer_choice][0]][open_spots[computer_choice][1]] = 'X'   
    return board
 
 
def start_game():
    print("Welcome to a game of a tic-tac-toe, are you ready to face this enemy?")
    print("""Your enemy gonna uses the X's, while youre using the O's
            Your enemy starts with his first move""")
    # sign should be "X" or "O"
    board = [[EMPTY for row in range(3)]for column in range(3)]
    board[1][1] = 'X'
    count = 1
    display_board(board)
    while count != 9:
        board = enter_move(board)
        count += 1 
        display_board(board)
        if victory_for(board, 'O'):
            print("The player using O's is the winner")
            break
        board = draw_move(board)
        count += 1
        print("Your enemy did the following")
        display_board(board)
        if victory_for(board, 'X'):
            print("The player using X's is the winner")
            break
    else:
        print("No Winners here")
 
 
 
 
# The program itself, the concept:
start_game()
answer = input("The game ends, wanna restart, type Yes for a restart and No for game to end")
yes_responses = ["yes", "y"]
while answer.lower() in yes_responses:
    start_game()
    answer = input("The game ends, wanna restart, type Yes for a restart and No for game to end")
 
 
print("Thank you for playing")
