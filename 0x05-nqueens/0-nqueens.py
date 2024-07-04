#!/usr/bin/env


def solveNQueens(n):
    col = set()  # To ensure save already used column
    posDiag = set()  # (r + c) to check diagonally downLeft-upRight
    negDiag = set()  # (r - c) to check diagonally upLeft-DownRight

    tmpResult = []
    result = []
    chessBoard = [["."] * n for _ in range(n)]

    def backtrackAlgorithm(r):
        if r == n:
            result.append(tmpResult.copy())  # copy tmpR to not clean result
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            tmpResult.append([r, c])
            backtrackAlgorithm(r + 1)

            # Backtracking by removing last items
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            tmpResult.pop()

    backtrackAlgorithm(0)
    return result


if __name__ == '__main__':
    from sys import argv

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    result = solveNQueens(n)
    [print(i) for i in result]
