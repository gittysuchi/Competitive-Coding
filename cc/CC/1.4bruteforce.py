def search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
nums = list(map(int, input("Enter the sorted array (space-separated): ").split()))
target = int(input("Enter the target number: "))
position = search(nums, target)
print("Insert/Search Position:", position)
