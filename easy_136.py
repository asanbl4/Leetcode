from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cur = nums[0]
        for i in range(1, len(nums)):
            cur ^= nums[i]
        return cur
solution = Solution()
print(solution.singleNumber([1,3,1,4,3]))