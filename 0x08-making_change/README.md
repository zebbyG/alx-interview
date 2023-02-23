## Making Change

- A pile of coins of different values, determining the fewest number of coins needed to meet a given amount total

## Tests :heavy_check_mark:


## Tasks :page_with_curl:

- Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

    - Prototype: `def makeChange(coins, total)`
    - Return: fewest number of coins needed to meet total
    - If total is `0` or less, return `0`
    - If total cannot be met by any number of coins you have, return `-1`
    - coins is a list of the values of the coins in your possession
    - The value of a coin will always be an integer greater than `0`
    - You can assume you have an infinite number of each denomination of coin in the list
    - Your solution’s runtime will be evaluated in this task

## Solution :page_with_curl:

- The function first checks if the total is `0` or `negative`, in which case it returns `0`. It then creates a list `min_coins` to store the minimum number of coins needed for each sub-total from `0` to total. The list is initialized with a large value for `sub-totals` that cannot be achieved.

- The function then iterates over all sub-totals from `1` to total and tries each coin value to see if it can be used to make the `sub-total`. If a coin can be used, the minimum number of coins needed for the sub-total is updated based on the minimum number of coins needed for the sub-total minus the coin value (i.e., `min_coins``[sub_total - coin]`) plus one (i.e., the coin being used).

- Finally, the function checks if the minimum number of coins needed for the given total is still greater than the total. If it is, it means the total cannot be achieved with the given coins, so the function returns `-1`. Otherwise, it returns the minimum number of coins needed.

- This implementation has a runtime complexity of `O(total * n)`, where n is the number of coins in the list. However, it uses dynamic programming to avoid recalculating solutions for sub-problems, which makes it much more efficient than a naive recursive approach.
