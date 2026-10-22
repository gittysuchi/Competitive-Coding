def climbStairs(n):
    if n == 0 or n == 1:
        return 1

    return climbStairs(n - 1) + climbStairs(n - 2)


n = int(input("Enter number of stairs: "))
print("Number of ways:", climbStairs(n))