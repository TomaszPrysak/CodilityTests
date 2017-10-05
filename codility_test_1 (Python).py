# -*- coding: utf-8 -*-

def solution(list):
    num_equili_point = 0
    list_of_equili_point = []
    a = len(list)
    b = len(list[0])
    above = 0
    below = 0
    left = 0
    right = 0
    for row in range(1, a-1):
        for x_above in range(0, row):
            above = above + sum(list[x_above])
        for x_below in range(row+1, a):
            below = below + sum(list[x_below])
        if (above == below):
            for col in range(1, b-1):
                for y_left in range(0, col):
                    for x_left in range(0, a):
                        left = left + list[x_left][y_left]
                for y_right in range(col+1, b):
                    for x_right in range(0, a):
                        right = right + list[x_right][y_right]
                if (left == right):
                    list_of_equili_point.append([row,col])
        above = 0
        below = 0
        left = 0
        right = 0
    if (len(list_of_equili_point) != 0):
        num_equili_point = len(list_of_equili_point)
    return num_equili_point

A = [[2, 7, 5], [3, 1, 1], [2, 1, -7], [0, 2, 1], [1, 6, 8]]

print(solution(A))