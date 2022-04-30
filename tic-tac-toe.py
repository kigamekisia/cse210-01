'''
Tic-Tac-Toe
Author: Kigame Kisia
'''
def main():
    player_letter = player_option("")
    board = create_board()
    while not (win(board) or draw(board)):
        display_board(board)
        input_letter(player_letter, board)
        player_letter = player_option(player_letter)
    display_board(board)
    print("Thank you for playing. Goodbye!") 
def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board
def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
def win(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def input_letter(player_letter, board):
    square = int(input(f"Turn for '{player_letter}' to choose a square (1-9): "))
    board[square - 1] = player_letter

def player_option(option):
    if option == "" or option == "o":
        return "x"
    elif option == "x":
        return "o"
if __name__ == "__main__":
    main()