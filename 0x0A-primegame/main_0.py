#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(1, [4])))
print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(3, [0, 0, 1])))
print("Winner: {}".format(isWinner(1, [64])))
print("Winner: {}".format(isWinner(-1, [10])))

