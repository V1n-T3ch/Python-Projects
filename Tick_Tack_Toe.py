import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column values.")

def computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human_player = "X"
    computer_player = "O"
    current_player = human_player

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        if current_player == human_player:
            row, col = player_move(board)
        else:
            print("Computer's turn...")
            row, col = computer_move(board)

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        current_player = human_player if current_player == computer_player else computer_player

if __name__ == "__main__":
    play_game()
