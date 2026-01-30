class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {(i+1): 0 for i in range(n)}
        def dfs(num):
            nonlocal dp
            if num <= 2:
                dp[num] = num
                return dp[num]
            if dp[num] != 0:
                return dp[num]
            dp[num] =  dfs(num - 1) + dfs(num - 2)
            return dp[num]
        dfs(n)
        # print(dp)
        return dp[n]

solution = Solution()
print(solution.climbStairs(35))