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
    elif (n == 2):
        return True
    elif (n % 2 == 0):
        return False
    else:
        sqrtOfNumber = int(n ** (1/2))
        for i in range(3, sqrtOfNumber):
            if (n % i == 0):
                print(i)
                return False
        return True


def isWinner(x, nums):
    """ Determine who is the winner between Maria and Ben """
    users = {'Maria': 0, 'Ben': 0}
    for round in nums:
        currentPlayer = True
        availableSlots = list(range(2, round + 1))
        # print('avalable slots:', availableSlots)
        while availableSlots:
            if isPrime(availableSlots[0]):
                currentPlayer = not currentPlayer
            availableSlots.remove(availableSlots[0])
        if not currentPlayer:
            users['Maria'] = users.get('Maria', 0) + 1
        else:
            users['Ben'] = users.get('Ben', 0) + 1
        # print(f'Winner for this round {round} is: {users}')

    # print(users)
    winner = max(users, key=users.get)
    return winner
