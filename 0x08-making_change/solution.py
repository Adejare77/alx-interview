#!/usr/bin/env

def makeChange(coins, total):
    """ Determine the fewest number of coins needed
    to meet a given amount total """
    if total <= 0:
        return 0

    n = len(coins)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        # for j in range(n):
        #     if coins[j] <= i:
        #         dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    print(dp)
    return dp[total] if dp[total] != float('inf') else -1

print(makeChange([1,2,5,6], 15))


#!/usr/bin/python3
""" making change """

def makeChange(coins, total):
    """ List all possible combinations of coins to make up the given total """
    if total <= 0:
        return []

    n = len(coins)
    # Initialize dp array where each element is a list of possible combinations
    dp = [[] for _ in range(total + 1)]
    dp[0] = [[]]  # Base case: one way to make 0, which is using no coins

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                for combo in dp[i - coin]:
                    dp[i].append(combo + [coin])

    return dp[total]

# print(makeChange([1, 2, 5, 6], 16))
