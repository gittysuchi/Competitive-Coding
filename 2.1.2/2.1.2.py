def combinationSum(candidates, target):
    result = set()

    def solve(remaining, current):
        if remaining == 0:
            result.add(tuple(sorted(current)))
            return

        if remaining < 0:
            return

        for c in candidates:
            solve(remaining - c, current + [c])

    solve(target, [])

    return [list(combination) for combination in result]


candidates = list(map(int, input("Enter candidates: ").split()))
target = int(input("Enter target: "))

result = combinationSum(candidates, target)

print("Combinations are:")

for combination in result:
    print(combination)