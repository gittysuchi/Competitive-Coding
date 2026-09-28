class Solution:
    def findMin(self, arr):
        temp = arr[0]

        for i in range(len(arr)):
            if arr[i] < temp:
                temp = arr[i]

        return temp


arr = [5, 3, 8, 1, 9, 2]

solution = Solution()
print(solution.findMin(arr))