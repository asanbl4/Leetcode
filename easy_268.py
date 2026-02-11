from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums2 = [i for i in range(len(nums) + 1)]
        sumXOR = 0
        for i in range(len(nums)):
            sumXOR += nums2[i] - nums[i]
        return sumXOR + nums2[-1]
solution = Solution()
print(solution.missingNumber([3,1,0]))