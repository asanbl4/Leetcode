from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [1000] * (len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        def dfs(curPosition):
            nonlocal dp, cost
            if dp[curPosition] != 1000:
                return dp[curPosition]
            if curPosition <= 1:
                dp[curPosition] = cost[curPosition]
                return cost[curPosition]

            curCost = min(dfs(curPosition - 1) + cost[curPosition], dfs(curPosition - 2) + cost[curPosition])
            dp[curPosition] = curCost
            return dp[curPosition]
        dfs(len(cost) - 1)
        return min(dp[len(cost) - 2], dp[len(cost) - 1])

solution = Solution()
print(solution.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))
