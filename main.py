def printBoard(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def winCheck(board, player):
    winCombos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in winCombos)

def isDraw(board):
    return all(cell != " " for cell in board)

def playGame():
    board = [" "] * 9
    currentPlayer = "X"

    while True:
        printBoard(board)
        try:
            move = int(input(f"Player {currentPlayer}, enter position (0-8): "))
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move, try again.")
                continue

            board[move] = currentPlayer

            if winCheck(board, currentPlayer):
                printBoard(board)
                print(f"Player {currentPlayer} wins!")
                break

            if isDraw(board):
                printBoard(board)
                print("It's a draw!")
                break

            currentPlayer = "O" if currentPlayer == "X" else "X"
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    playGame()