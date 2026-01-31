from collections import defaultdict


class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = defaultdict(lambda: 0)
        def dfs(substring: str):
            nonlocal dp
            if dp[substring] != 0:
                return dp[substring]
            if len(substring) <= 1:
                dp[substring] = len(substring)
                return dp[substring]
            def isPalindrome(string):
                return string == string[::-1]
            dp[substring] = dfs(substring[1:])
            copySubstring = substring
            while copySubstring:
                dp[substring] += int(isPalindrome(copySubstring))
                copySubstring = copySubstring[:-1]
            return dp[substring]
        dfs(s)
        return dp[s]

solution = Solution()
print(solution.countSubstrings("a"))