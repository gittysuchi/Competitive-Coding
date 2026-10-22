def findDuplicate(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return nums[i]


nums = list(map(int, input("Enter elements: ").split()))
print("Duplicate:", findDuplicate(nums))