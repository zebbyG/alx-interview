#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Create a table to store the minimum number of coins
    for each sub-total"""
    if total <= 0:
        return 0
    """    The table is initialized with a large value (total + 1)
    for sub-totals
    that cannot be achieved
    """
    min_coins = [total + 1] * (total + 1)
    min_coins[0] = 0

    """Iterate over all sub-totals from 1 to the given total"""
    for sub_total in range(1, total + 1):
        """Try each coin value and see if it can be used to make
        the sub-total"""
        for coin in coins:
            if coin <= sub_total:
                """If the coin can be used, update the minimum
                number of coins needed"""
                min_coins[sub_total] = min(min_coins[sub_total],
                                           1 + min_coins[sub_total - coin])

    """If the final entry in the table has not been updated,
    it means the total cannot be achieved"""
    if min_coins[total] > total:
        return -1
    else:
        return min_coins[total]
