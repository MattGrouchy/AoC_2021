'''
Project: day04
Created Date: Monday December 20th 2021
Author: Matthew Grouchy
'''
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

    # iterate through each of the draw_numbers
    for number in draw_numbers:
        count += 1
        # loop through each board
        for bingo_board in boards:
            # loop through each boards row
            for row in bingo_board:
                for grid in row:
                    if (grid[0] == number):
                        grid[1] = 1

    print("Count: ", count, "len(draw_numbers): ", len(draw_numbers))

    print(boards[0])


def day04_main():
    data = load_data("day04/input_day04.txt")
    part1(data)
