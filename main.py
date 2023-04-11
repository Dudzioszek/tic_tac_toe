def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
        print("-------------")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    #dia
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    # first row then columns included there
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    players = ["X", "O"]

    current_player = players[0]


    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        print("It's", current_player, "'s turn.")

        row = int(input("Enter the row (1-3): ")) - 1
        col = int(input("Enter the column (1-3): ")) - 1


        if board[row][col] != " ":
            print("That space is already taken. Try again.")
            continue


        board[row][col] = current_player
        print_board(board)
        if check_win(board, current_player):
            print(current_player, "wins!")
            print("Made by Stanislaw Dutkiewicz")
            break
        
        # tie scenario
        if all([board[i][j] != " " for i in range(3) for j in range(3)]):
            print("It's a tie!")
            break

        # switch player
        current_player = players[(players.index(current_player) + 1) % 2]

tic_tac_toe()
