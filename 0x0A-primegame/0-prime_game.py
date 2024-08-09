#!/usr/bin/python3
"""Prime Game"""


def isPrime(n):
    """check if n is a prime number or not

    Args:
        n (int): The number to check for

    Returns:
        bool: true if it is prime, else false
    """
    if (n < 2):
        return False
    elif (n <= 3):
        return True
    elif (n % 2 == 0 or n % 3 == 0):
        return False
    else:
        sqrtOfNumber = int(n ** (1/2))
        for i in range(5, sqrtOfNumber + 1, 2):
            if (n % i == 0):
                return False
        return True


def isWinner(x, nums):
    """ Determine who is the winner between Maria and Ben """
    if x < 1 or not nums:
        return None
    # sort the given arrays. The purpose is to avoid repetition of
    # predetermined prime numbers by previous round (prev_round)
    sorted_nums = sorted(nums)  # sort them to know who won last
    users = {'Maria': 0, 'Ben': 0}
    prev_round = None  # previously determined round
    # True means Maria's turn, while False means Ben's turn to play
    currentPlayer = True

    for round in sorted_nums:
        if prev_round:
            availableSlots = list(range(prev_round + 1, round + 1))
        else:
            availableSlots = list(range(2, round + 1))
        prev_round = round
        while availableSlots:
            if isPrime(availableSlots[0]):
                currentPlayer = not currentPlayer
            availableSlots.remove(availableSlots[0])

        if not currentPlayer:
            users['Maria'] += 1
        else:
            users['Ben'] += 1

    if users['Maria'] == users['Ben']:
        return None
    winner = max(users, key=users.get)
    return winner
