from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]
        def dfs(c):
            nonlocal dp
            if dp[c] != 0:
                return dp[c]
            if c <= 1:
                dp[c] = c
                return dp[c]
            if dp[c] == 0:
                dfs(c // 2)
            dp[c:] = [i + 1 for i in dp[:c]]
        pow = -1
        m = n
        while m:
            pow += 1
            m //= 2
        if pow == -1:
            return [0]
        dfs(2 ** pow)
        return dp[:n + 1]



solution = Solution()
print(solution.countBits(0))
[0,1, 1,2, 1,2,2,3, 1,2,2,3,2,3,3,4, 1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5]