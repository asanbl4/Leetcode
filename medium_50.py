class Solution:
    def myPow(self, x: float, n: int) -> float:
        dp = {}
        def dfs(x, n):
            if (x, n) in dp:
                return dp[(x, n)]
            if n == 0:
                dp[(x, 0)] = 1
                return 1
            if n == 1:
                dp[(x, 1)] = x
                return x
            if n == -1:
                dp[(x, -1)] = 1/x
                return 1/x
            if n % 2:
                if n < 0:
                    dp[(x, n)] = dfs(x, n + 1) / x
                else:
                    dp[(x, n)] = x * dfs(x, n - 1)
            else:
                res = dfs(x, n / 2)
                dp[(x, n)] = res * res
            return dp[(x, n)]
        return dfs(x, n)

solution = Solution()
print(solution.myPow(2,  30))
