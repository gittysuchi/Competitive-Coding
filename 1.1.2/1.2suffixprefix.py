def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]
    
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]
    
    return answer  
nums = input("Enter the array: ")
arr = list(map(int, nums.split()))

print(product_except_self(arr))
