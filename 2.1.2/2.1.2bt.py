from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] <= remaining:
                    current.append(candidates[i])
                    backtrack(i, current, remaining - candidates[i])
                    current.pop()

        backtrack(0, [], target)

        return result


candidates = list(map(int, input("Enter candidates: ").split()))
target = int(input("Enter target: "))

sol = Solution()

result = sol.combinationSum(candidates, target)

print("Combinations are:")
for combination in result:
    print(combination)