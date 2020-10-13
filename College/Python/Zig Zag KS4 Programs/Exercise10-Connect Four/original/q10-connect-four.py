def draw(grid):
    print("")
    print("1 2 3 4 5") # Print column headers
    print("| | | | |")
    print(grid[0][0], grid[0][1], grid[0][2], grid[0][3], grid[0][4], "- row 1")
    print(grid[1][0], grid[1][1], grid[1][2], grid[1][3], grid[1][4], "- row 2")
    print(grid[2][0], grid[2][1], grid[2][2], grid[2][3], grid[2][4], "- row 3")
    print(grid[3][0], grid[3][1], grid[3][2], grid[3][3], grid[3][4], "- row 4\n")

def add_piece(grid, column, row, player):
    if player == 1:
        piece = "B"
    else:
        piece = "R"
    grid[row][column] = piece
    return grid

#- MAIN PROGRAM ----------------------------------------------

board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
won = False

draw(board)

while not won == True:

    player = 1

    print("It is player " + str(player) + "'s go.")
    c_choice = int(input("Enter the column number. "))
    r_choice = int(input("Enter the row number. "))

    board = add_piece(board, c_choice, r_choice, player)

    if player == 1:
        player = 2
    else:
        player = 1

    draw(board)

print("Player " + str(player) + " has won!")
input("Press enter to exit.")
