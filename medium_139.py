from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(substring: str):
            print(substring)
            nonlocal dp, wordDict
            if not substring:
                return True
            if substring in dp:
                return dp[substring]
            dp[substring] = False
            for word in wordDict:
                if substring.startswith(word):
                    dp[substring] = dfs(substring[len(word):])
                    if dp[substring]:
                        return True
            return dp[substring]
        return dfs(s)
        # print(dp)

solution = Solution()
print(solution.wordBreak(s = "abcd", wordDict = ["a","abc","b","cd"]))