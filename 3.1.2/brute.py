def frogJump(n, k, height):
    if n == 0:
        return 0

    min_cost = float('inf')

    for jump in range(1, k + 1):
        if n - jump >= 0:
            cost = frogJump(n - jump, k, height) + abs(height[n] - height[n - jump])
            min_cost = min(min_cost, cost)

    return min_cost


height = list(map(int, input("Enter heights: ").split()))
k = int(input("Enter K: "))

n = len(height)

print("Minimum cost:", frogJump(n - 1, k, height))