import math

board = [' ' for _ in range(9)]


def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')


def winner(board, player):
    win_cond = [
        [0,1,2], [3,4,5], [6,7,8], # Rows
        [0,3,6], [1,4,7], [2,5,8], # Columns
        [0,4,8], [2,4,6]           # Diagonals
    ]
    for cond in win_cond:
        if all(board[i] == player for i in cond):
            return True
    return False


def is_full(board):
    return ' ' not in board


def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']


def minimax(board, depth, is_maximizing):
    if winner(board, 'O'):
        return 1
    elif winner(board, 'X'):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score
def ai_move():
    best_score = -math.inf
    move = None
    for i in available_moves(board):
        board[i] = 'O'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    board[move] = 'O'


def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Spot already taken. Try again.")
        except (IndexError, ValueError):
            print("Invalid input. Enter a number from 1 to 9.")

def play_game():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()
    
    while True:
        human_move()
        print_board()
        if winner(board, 'X'):
            print("You win! 🎉")
            break
        if is_full(board):
            print("It's a tie!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()
        if winner(board, 'O'):
            print("AI wins! 🤖")
            break
        if is_full(board):
            print("It's a tie!")
            break


if __name__ == "__main__":
    play_game()
