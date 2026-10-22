def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))

print("Minimum coins:", coinChange(coins, amount))