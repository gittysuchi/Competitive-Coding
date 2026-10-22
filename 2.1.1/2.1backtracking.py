from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            result.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])

        return result


nums = list(map(int, input("Enter the elements: ").split()))

sol = Solution()
result = sol.subsets(nums)
print("All subsets are:")
for subset in result:
    print(subset)