def find(board,choice):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if choice == board[i][j]:
                return i, j

grid = [["a","X","c","d"],["e","f","g","h"],["i","j","k","l"],["m","n","o","p"]]

while True:
    print(grid)
    choice = input("Enter a letter: ")
    direction = input("Enter a direction (u,d,l,r): ")

    row, column = find(grid, choice)

    if direction == "r":
        if column + 2 < len(grid[0]):
            if grid[row][column + 2] == "X":
                grid[row][column] = "X"
                grid[row][column + 1] = "X"
                grid[row][column + 2] = choice

    if direction == "l":
        if column - 2 >= 0:
            if grid[row][column - 2] == "X":
                grid[row][column] = "X"
                grid[row][column - 1] = "X"
                grid[row][column - 2] = choice

    if direction == "u":
        if row - 2 >= 0:
            if grid[row - 2][column] == "X":
                grid[row][column] = "X"
                grid[row - 1][column] = "X"
                grid[row - 2][column] = choice

    if direction == "d":
        if row + 2 < len(grid):
            if grid[row + 2][column] == "X":
                grid[row][column] = "X"
                grid[row + 1][column] = "X"
                grid[row + 2][column] = choice
                
input("Press enter to exit.")
