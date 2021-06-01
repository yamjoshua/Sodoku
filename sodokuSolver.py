# Joshua Yam jy2223 N12174023
# CS4613 Project 2 - Sudoku Solver
# Python 2.7
# May 18th, 2019

from __future__ import print_function
import random


# Has the solution been found? '0's represent the empty tiles on the board. If there are no '0's the solution has been found.
def is_Solved(board):
    is_Solved = True
    for row in board:
        for tile in row:
            if tile == '0':
                is_Solved = False
    return is_Solved


# Creates a 9x9 board with all possible values for each tile
def init_Constrain(board):
    constrain = []
    row = []
    for i in range(9):
        for j in range(9):
            if board[i][j] != '0':
                row.append(['0'])
            else:
                row.append(possible_Values(board, i, j))
        constrain.append(row)
        row = []
    return constrain


# Given a coordinate generate all possible values
def possible_Values(tile, x, y):
    # Full Domain
    all_Values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if tile[x][y] == '0':
        for i in range(1, 10):
            # Remove all values that appear in the row from the Domain
            if str(i) in tile[x]:
                try:
                    all_Values.remove(str(i))
                except:
                    continue
        for i in range(9):
            # Remove all values that appear in the column from the Domain
            try:
                all_Values.remove(tile[i][y])
            except:
                continue
    else:
        return tile[x][y]

    # Remove all values that appear in the 3x3 block from the Domain
    row_corner = 0
    col_corner = 0
    if x >= 0 and x <= 2:
        row_corner = 0
    elif x >= 3 and x <= 5:
        row_corner = 3
    else:
        row_corner = 6
    if y >= 0 and y <= 2:
        col_corner = 0
    elif y >= 3 and y <= 5:
        col_corner = 3
    else:
        col_corner = 6

    for i in range(row_corner, row_corner + 3):
        for j in range(col_corner, col_corner + 3):
            if tile[i][j] != '0':
                try:
                    all_Values.remove(tile[i][j])
                except:
                    continue
    return all_Values


# Return all the coordinates of the empty tiles
def get_Blank(board):
    blank_Tiles = []
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == '0':
                blank_Tiles.append([i, j])
    return blank_Tiles


# Backtracking with Forward checking and using the MRV heuristic with the Degree heuristic as a TieBreaker
def search(board):
    """

    :type board: object
    """

    if is_Solved(board):
        write_Board(board)  # write to file if solution is found
        return 1
    mrv_Tiles = mrv(board)  # Use MRV heuristic function

    if len(mrv_Tiles) == 1:  # No Tiebreaker
        tile = mrv_Tiles[0]
    else:
        # If there is a tiebreaker use the degree heuristic to find tile with greatest value
        tile_Degrees = []
        for i in mrv_Tiles:
            degree = get_degree(board, i[0], i[1])
            tile_Degrees.append(degree)

            maxTile = max(tile_Degrees)
            maxTiles = []
            for i in range(len(tile_Degrees)):
                val = tile_Degrees[i]
                if val == maxTile:
                    maxTiles.append(mrv_Tiles[i])
            tile = maxTiles[0]
    row = tile[0]
    col = tile[1]

    # Backtracking
    constraint = init_Constrain(board)
    vals = constraint[row][col]
    while len(vals) != 0:
        val = random.choice(vals)
        vals.remove(val)
        if forward_checking(constraint, val, row, col):
            board[row][col] = val
            if search(board):
                return 1
            else:
                board[row][col] = '0'
    return 0


# See if value is the only one in row, column, and block
def forward_checking(constraint, val, row, col):
    if len(constraint[row][col]) == 1:
        if constraint[row][col] == val:
            return False
    return True


# Minimum remaining value heuristic. Find the most constrained tiles
def mrv(board):
    emptyTile = get_Blank(board)
    empty_TileLength = [len(possible_Values(board, i[0], i[1])) for i in emptyTile]
    mrv_Tiles = []

    minimum = min(empty_TileLength)
    min_Indexes = [i for i, x in enumerate(empty_TileLength) if x == minimum]
    for i in min_Indexes:
        mrv_Tiles.append(emptyTile[i])
    return mrv_Tiles


# Given a coordinate find number of constraints on other variables
def get_degree(board, x, y):
    degree = 0
    for i in range(9):
        # How many blank tiles in row
        if board[x][i] == '0':
            degree += 1
        # How many blank tiles in column
        if board[i][y] == '0':
            degree += 1

    # How many blank tiles in block
    row_corner = 0
    col_corner = 0
    if x >= 0 and x <= 2:
        row_corner = 0
    elif x >= 3 and x <= 5:
        row_corner = 3
    else:
        row_corner = 6
    if y >= 0 and y <= 2:
        col_corner = 0
    elif y >= 3 and y <= 5:
        col_corner = 3
    else:
        col_corner = 6

    for i in range(row_corner, row_corner + 3):
        for j in range(col_corner, col_corner + 3):
            if board[i][j] == '0':
                degree += 1
    return degree


# Write to File
def write_Board(board):
    file_name = raw_input('Name of Output file: ')
    with open(file_name, "w") as f:

        for i in board:
            for j in i:
                f.write(j)
                f.write(' ')
            f.write('\n')
    f.close()


def print_before_after(before, after):
    for row in range(len(before)):
        for col in range(len(before[0])):
            print(before[row][col] + ' ', end='')
        print('   |   ', end='')
        for col in range(len(after[0])):
            print(after[row][col] + ' ', end='')
        print('\n', end='')


