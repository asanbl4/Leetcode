from typing import List
from collections import defaultdict

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(money):
            nonlocal coins
            if money < 0:
                return -1
            if money == 0:
                return 0
            if money in dp:
                return dp[money]

            min_count = float('inf')

            for coin in coins:
                res = dfs(money - coin)
                if res != -1:
                    min_count = min(min_count, res + 1)

            dp[money] =  min_count if min_count != float('inf') else -1
            return dp[money]

        return dfs(amount)

solution = Solution()
# print(solution.coinChange(coins = [2], amount = 3))
print(solution.coinChange(coins = [186,419,83,408], amount = 6249))