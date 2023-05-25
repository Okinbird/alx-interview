#!/usr/bin/python3
""" Description: The N queens puzzle is the challenge of placing
                  N non-attacking queens on an N×N chessboard.
                  Write a program that solves the N queens problem. """
import sys


class NQueens:
    """ N Queens class """

    def __init__(self, n):
        """ Constructor argument """
        self.n = n
        self.x = [0 for i in range(n + 1)]
        self.res = []

    def isSafe(self, k, i):
        """ Check if a place is safe """
        for j in range(1, k):
            if self.x[j] == i or \
               abs(self.x[j] - i) == abs(j - k):
                return 0
        return 1

    def solveNQ(self, k):
        """ Solve the nqueen """
        for i in range(1, self.n + 1):
            if self.isSafe(k, i):
                self.x[k] = i
                if k == self.n:
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.res.append(solution)
                else:
                    self.solveNQ(k + 1)
        return self.res


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

number = sys.argv[1]

try:
    number = int(number)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if number < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueens(number)
result = queen.solveNQ(1)

for i in result:
    print(i)
