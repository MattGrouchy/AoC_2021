'''
Project: day05
Created Date: Tuesday December 21st 2021
Author: Matthew Grouchy
'''
from helpers.utils import load_data
import re


def part1(data):
    print("part1")

    # need to determine the number of points where at least two lines overlap

    # make a dict. If a point is already in the dict then increment it's value. If not then create a
    # new key are that point and set the value to 1.
    # dict with keys for y points that holds a dict for x points

    points = {}
    # print(data[0:5])

    def add_points_horizontal(x1, y1, x2, y2):

        min = x1 if x1 < x2 else x2
        max = x2 if x2 > x1 else x1

        if y1 in points.keys():
            for i in range(min, max+1):
                if i in points[y1].keys():
                    points[y1][i] += 1
                    # print("overlap")
                else:
                    points[y1][i] = 1
        else:
            # make a new dict at y1
            points[y1] = {}
            for i in range(min, max+1):
                points[y1][i] = 1

    def add_points_vertical(x1, y1, x2, y2):

        min = y1 if y1 < y2 else y2
        max = y2 if y2 > y1 else y1

        # loop through all the y values in the vertical line
        for i in range(min, max+1):
            # if y is already in points
            if i in points.keys():
                # check if x is already in y
                if x1 in points[i].keys():
                    points[i][x1] += 1
                else:
                    points[i][x1] = 1
            else:
                # make dict at y and add x
                points[i] = {}
                points[i][x1] = 1

    for line_eq in data:
        x1, y1, x2, y2 = [int(x) for x in re.split(', | -> |,', line_eq)]

        # print(x1, y1, x2, y2)
        if (y1 == y2):
            add_points_horizontal(x1, y1, x2, y2)
        elif (x1 == x2):
            add_points_vertical(x1, y1, x2, y2)

    danger_spot = 0

    # need to loop through points and increment for every point that is dangerous
    # print(points)

    for y in points:
        for x in points[y]:
            if points[y][x] > 1:
                danger_spot += 1

    print("danger_spots:", danger_spot)


def day05_main():
    print("day05")
    data = load_data("day05/input_day05.txt")
    part1(data)
