def display_board(board): #ale letztes nur visuell
    trennzeile = "+-------+-------+-------+"
    zw_trennzeile = "|       |       |       |"
    print(trennzeile)
    for row in range(len(board)):
        inhaltszeile = f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |"
        print(zw_trennzeile)
        print(inhaltszeile)
        print(zw_trennzeile)
        print(trennzeile)

        
def enter_move(board):
    new_move = int(input("Show me your next move: "))
    if new_move > 9 or new_move < 1:
        print("This value is not choosable")
        return enter_move(board)
    elif board[(new_move-1)//3][(new_move -1) % 3] == 'X' or board[(new_move-1)//3][(new_move -1) % 3] == 'O':
        print("You cant choose this value")
        return enter_move(board)
    else:
        board[(new_move-1)//3][(new_move -1) % 3] = 'O'
        return board


def make_list_of_free_fields(board):
    tuple_board = []
    for i in range (9):
        if board[(i)//3][(i) % 3] == EMPTY:
            tuple_board.append(((i)//3,(i) % 3))
    return tuple_board



def victory_for(board, sign):
    alle_linien = [
    [(0,0),(0,1),(0,2)],   # Zeile 0
    [(1,0),(1,1),(1,2)],   # Zeile 1
    [(2,0),(2,1),(2,2)],   # Zeile 2
    [(0,0),(1,0),(2,0)],   # Spalte 0
    [(0,1),(1,1),(2,1)],   # Spalte 1
    [(0,2),(1,2),(2,2)],   # Spalte 2
    [(0,0),(1,1),(2,2)],   # Diagonale
    [(0,2),(1,1),(2,0)],   # Diagonale
]
    for linie in alle_linien:
        treffer = 0
        for koordinate in linie:
            if board[koordinate[0]][koordinate[1]] == sign:
                treffer = treffer + 1
        if treffer == 3:
            return True
    return False

    
        
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    freie_felder = make_list_of_free_fields(board)
    pc_move =(randrange(len(freie_felder)))
    board[freie_felder[pc_move][0]][freie_felder[pc_move][1]] = 'X'
    return board




#The programm itself, the concept:
from random import randrange
EMPTY = "-"
def spiel_starten():
    print("Welcome to a game of a tic-tac-toe, are you ready to face this enemy?")
    print("""Your enemy gonna uses the X's, while youre using the O's
            Your enemy starts with his first move""")
    #sign soll "X" oder "O" sein
    board = [[EMPTY for row in range(3)]for column in range(3)] #Empty noch nicht definiert (was ist Empty überhaupt?
    #Ich muss die Zeilen den Zahlen zuordnen bzw. festlegen count = number
    board[1][1] = 'X'
    count = 1
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
    if count == 9:
        print("No Winners here")

spiel_starten()
answer = input("The game ends, wanna restart, type Yes for a restart and No for game to end")
while answer == 'Yes':
    spiel_starten()
    answer = input("The game ends, wanna restart, type Yes for a restart and No for game to end")
    if answer == 'No':
        break

print("Thank you for playing")
