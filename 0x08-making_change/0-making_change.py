#!/usr/bin/python3
""" Module making_change """


def makeChange(coins, total):
    """ Function that returns min number of coins """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make change for 0
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each amount from coin to total
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, means the total cannot be met
    if dp[total] == float('inf'):
        return -1

    return dp[total]
