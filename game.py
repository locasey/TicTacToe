
board_width = 3
board_height = 3

def new_board():
    board = []
    for i in range(board_width):
        column = []
        for i in range(board_height):
            column.append(None)
        board.append(column)

    return board

board = new_board()
print(board)

## TODO: Get atom working, Stop looking at mans code, get player input
