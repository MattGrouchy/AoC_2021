'''
Project: day04
Created Date: Monday December 20th 2021
Author: Matthew Grouchy
'''
from os import supports_follow_symlinks
from helpers.utils import load_data


def part1(data):
    # need to create 5x5 grids for bingo boards. I need to hold onto the data within each spot to multiply the row/column
    # afterward
    print("part 1")
    # every number for a bingo board could be a list with [number, marked]
    draw_numbers = [val for val in data[0].split(",") if val]
    print(draw_numbers)

    boards = []
    board = []

    for i in range(2, len(data)):
        if (data[i] == ""):
            boards.append(board)
            board = []
        else:
            board.append([[val, 0] for val in data[i].split(" ") if val])

    # print(boards[0])
    count = 0

    boards_left = boards.copy()

    # iterate through each of the draw_numbers
    for number in draw_numbers:
        count += 1
        # loop through each board
        for i, bingo_board in enumerate(boards):
            # loop through each boards row
            for row in bingo_board:
                # loop through the square in row and check if needs to be marked
                for grid in row:
                    if (grid[0] == number):
                        grid[1] = 1
            # This board is now marked. Need to check if it is a winner.
            winner, seq_sum = is_board_winner(bingo_board)

            if (winner):
                print("The winning board was found at number:", count, "and is:")
                print(bingo_board)
                print("draw_number:", number)
                print("seq_sum: ", seq_sum, "product:", int(number) * seq_sum)
                boards_left[i] = False

            # Are all the entries to board_left False?
            boards_left_empty = True
            for still_there in boards_left:
                if still_there != False:
                    boards_left_empty = False

            if(boards_left_empty):
                print("Found the last board")
                return

    print("Count: ", count, "len(draw_numbers): ", len(draw_numbers))

    # TODO:
    # make a function to test each board after it is updated.


def get_sum(seq, index):
    sum = 0
    for x in seq:
        sum += int(x[index])
    return sum


def get_unmarked_sum(board):
    ''' function to loop through board and make sum of all numbers that are not marked'''
    sum = 0
    for row in board:
        for square in row:
            if(square[1] == 0):
                sum += int(square[0])
    return sum


def is_board_winner(board):
    ''' determines if board is winner. returns bool for winner and sum of winning sequence.'''
    # diagonals don't count so only need to look at rows and columns.
    # take the sum of every row, check if the sum is good.
    # Will invert the array by adding row[i] to column[i]
    # need to get the sum of all unmarked numbers on board
    columns = [[], [], [], [], []]

    # loop through each row in board
    for row in board:
        row_sum = get_sum(row, 1)
        # loop through square and add the square to row
        for i, square in enumerate(row):
            columns[i].append(square)
        # check if row mark sum is 5
        if (row_sum == 5):
            return True, get_unmarked_sum(board)

    # loop through each column in columns
    for column in columns:
        column_sum = get_sum(column, 1)
        # check if column mark sum is 5
        if (column_sum == 5):
            return True, get_unmarked_sum(board)

    return False, 0


def day04_main():
    data = load_data("day04/input_day04.txt")
    part1(data)
