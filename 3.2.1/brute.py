def coinChange(coins, amount):
    if amount == 0:
        return 0

    min_coins = float('inf')

    for coin in coins:
        if coin <= amount:
            result = coinChange(coins, amount - coin)

            if result != -1:
                min_coins = min(min_coins, result + 1)

    if min_coins == float('inf'):
        return -1

    return min_coins


coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))

print("Minimum coins:", coinChange(coins, amount))