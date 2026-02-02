from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max, cur_min = 1, 1

        for num in nums:
            temp = cur_max * num
            cur_max = max(temp, cur_min * num, num)
            cur_min = min(temp, cur_min * num, num)
            res = max(cur_max, res)
        return res

solution = Solution()
print(solution.maxProduct([-3,-1,-1]))


