from typing import List

from pydantic_core.core_schema import nullable_schema


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[0]
        dp[1] = nums[1]
        def dfs(curPos):
            nonlocal dp, nums
            if curPos < 0:
                return 0
            if dp[curPos] != -1:
                return dp[curPos]
            # print(curPos, curPos - 2, curPos - 3, nums[curPos])
            dp[curPos] = max(dfs(curPos - 2), dfs(curPos - 3)) + nums[curPos]
            return dp[curPos]
        lol = max(dfs(len(nums) - 1), dfs(len(nums) - 2))
        # print(dp)
        return lol

solution = Solution()
print(solution.rob(nums = [1,3,3]))
