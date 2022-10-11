def cell_checker(row, column, grid):
    if grid[row][column] > 0:
        return []

    possibilities = []

    for num in range(1, 10):
        exists = []

        for index in range(0, 9):

            if grid[row][index] == num:
                exists.append(num)

            if grid[index][column] == num:
                exists.append(num)

        start_row = row - row % 3
        start_column = column - column % 3

        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_column] == num:
                    exists.append(num)

        if len(exists) == 0:
            possibilities.append(num)

    return possibilities


def solve_sudoku(grid):
    filled_cells = 0
    no_single_num = 0

    for i in range(0, 9):
        for j in range(0, 9):
            possibilities = cell_checker(i, j, grid)

            if len(possibilities) == 1:
                grid[i][j] = possibilities[0]
            elif len(possibilities) == 0:
                filled_cells += 1
            elif len(possibilities) > 1:
                no_single_num += 1

    if filled_cells != 81 and filled_cells + no_single_num == 81:
        return False
    elif filled_cells != 81:
        return solve_sudoku(grid)
    else:
        return True


grid = [[0, 0, 4, 0, 5, 0, 0, 0, 0],
        [9, 0, 0, 7, 3, 4, 6, 0, 0],
        [0, 0, 3, 0, 2, 1, 0, 4, 9],
        [0, 3, 5, 0, 9, 0, 4, 8, 0],
        [0, 9, 0, 0, 0, 0, 0, 3, 0],
        [0, 7, 6, 0, 1, 0, 9, 2, 0],
        [3, 1, 0, 9, 7, 0, 2, 0, 0],
        [0, 0, 9, 1, 8, 2, 0, 0, 3],
        [0, 0, 0, 0, 6, 0, 1, 0, 0]]

if solve_sudoku(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No solution exists.")
