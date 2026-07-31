def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    
    for i in range(n):
        product = 1
        for j in range(n):
            if j != i:
                product *= nums[j]
        answer[i] = product
    
    return answer
nums = input("enter the array")
arr = list(map(int, nums.split()))

print(product_except_self(arr))