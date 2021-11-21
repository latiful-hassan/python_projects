from random import randrange

board = [["1", "2", "3"], ["4", "X", "6"], ["7", "8", "9"]]

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[0][0] +   "   |   " + board[0][1] +   "   |   " + board[0][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[1][0] +   "   |   " + "X" +   "   |   " + board[1][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[2][0] +   "   |   " + board[2][1] +   "   |   " + board[2][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    while True:

        user_move = int(input("Enter a position (1-9): "))

        if user_move < 1 or user_move > 9:
            print("Please enter a valid position (1-9).")
            continue
        elif str(user_move) not in board[0] and str(user_move) not in board[1] and str(user_move) not in board[2]:
            print("Position occupied - enter again.")
            continue
        elif user_move == 1:
            board[0][0] = "O"
        elif user_move == 2:
            board[0][1] = "O"
        elif user_move == 3:
            board[0][2] = "O"
        elif user_move == 4:
            board[1][0] = "O"
        elif user_move == 1:
            board[1][2] = "O"
        elif user_move == 1:
            board[2][0] = "O"
        elif user_move == 1:
            board[2][1] = "O"
        elif user_move == 1:
            board[2][2] = "O"

        break

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass


def victory_for(board, sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    pass


def draw_move(board):
    # The function draws the computer's move and updates the board.
    pass



display_board(board)
enter_move(board)
display_board(board)