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
    elif (n % 2 == 0):
        return False
    else:
        sqrtOfNumber = int(n ** (1/2))
        for i in range(3, sqrtOfNumber):
            if (n % i == 0):
                print(i)
                return False
        return True


# def isWinner(x, nums):
#     """ Determine who is the winner between Maria and Ben """
#     if not x or not nums:
#         return None

#     users = {'Maria': 0, 'Ben': 0}
#     for round in nums:
#         currentPlayer = True
#         availableSlots = list(range(2, round + 1))
#         while availableSlots:
#             if isPrime(availableSlots[0]):
#                 currentPlayer = not currentPlayer
#             availableSlots.remove(availableSlots[0])
#         if not currentPlayer:
#             users['Maria'] += 1
#         else:
#             users['Ben'] += 1

#     if users['Maria'] == users['Ben']:
#         return None
#     winner = max(users, key=users.get)
#     return winner

def isWinner(x, nums):
    """ Determine who is the winner between Maria and Ben """
    if not x or not nums:
        return None

    def play_game(n):
        availableSlots = set(range(2, n + 1))
        currentPlayer = True  # True for Maria, false for Ben
        while availableSlots:
            # Find the smallest prime number
            prime = min([num for num in availableSlots if
                         isPrime(num)], default=None)
            if not prime:
                break
            # Remove the prime and all its multiples
            availableSlots.difference_update(range(prime, n + 1, prime))
            currentPlayer = not currentPlayer

        # Determine the winner based on who cannot make a move
        return 'Maria' if not currentPlayer else 'Ben'

    users = {'Maria': 0, 'Ben': 0}
    for round in nums:
        winner = play_game(round)
        users[winner] += 1

    if users['Maria'] == users['Ben']:
        return None
    return max(users, key=users.get)
