def subsets(nums):
    result = []

    n = len(nums)
    for mask in range(2 ** n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])

        result.append(subset)

    return result
nums = list(map(int, input("Enter the elements: ").split()))

result = subsets(nums)

print("All subsets are:")

for subset in result:
    print(subset)