#!/usr/bin/python3
""" making change """


# def makeChange(coin, total):
#     """ change comes from within """
#     solution = []
#     result = []
#     tmp_list = coin.copy()
#     remainder = total
#     track_remainder = []
#     track = []

#     def dynamic_change_algorithm(coin, remainder, total):
#         """ determine the fewest number of coins needed to meet a
#         given amount total"""
#         if sum(solution) == total:
#             # result.append(solution.copy())
#             result.append(len(solution))
#             return result

#         while (max(tmp_list) > remainder):
#             tmp_list.remove(max(tmp_list))
#             # In case all tmp_list becomes empty
#             if not tmp_list:
#                 result.clear()
#                 track.clear()
#                 track_remainder.clear()
#                 return

#         max_list_val = max(tmp_list)
#         track.append(tmp_list.copy())
#         solution.append(max_list_val)
#         track_remainder.append(remainder)

#         remainder = remainder - max_list_val

#         if (remainder >= 0):
#             dynamic_change_algorithm(coin, remainder, total)

#         if track:
#             solution.pop()
#             last_item = track.pop()
#             last_item.remove(max(last_item))
#             remainder = track_remainder.pop()

#             if last_item:
#                 tmp_list.clear()
#                 tmp_list.extend(last_item)
#                 dynamic_change_algorithm(coin, remainder, total)

#     if total <= 0:
#         return 0

#     dynamic_change_algorithm(coin, remainder, total)

#     if not result:
#         return -1

#     return min(result)

def makeChange(coins, total):
    """ Determine the fewest number of coins needed
    to meet a given amount total """
    if total <= 0:
        return 0

    n = len(coins)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    return dp[total] if dp[total] != float('inf') else -1
