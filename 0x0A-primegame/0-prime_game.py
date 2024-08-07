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
    if not x or not nums:
        return None

    users = {'Maria': 0, 'Ben': 0}
    for round in nums:
        currentPlayer = True
        availableSlots = list(range(2, round + 1))
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
