#!/usr/bin/python3
"""
Defines function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Creates a list of lists of integers representing Pascal's triangle
    parameters:
        n [int]:
            the number of rows of Pascal's triangle to recreate
    return:
        [list of lists of ints]:
            representation of Pascal's triangle
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")
    a = [[] for i in range(n)]
    if n <= 0:
        return a
    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if (j == 0):
                    a[i].append(1)
                else:
                    a[i].append(a[i - 1][j] + a[i - 1][j - 1])
            elif (j == i):
                a[i].append(1)
    return a
