from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(lambda: 0)
        left, right = 0, 0
        ans = 0
        while right < len(s):
            counter[s[right]] += 1
            if len(set(counter.keys())) == 1:
                ans = max(ans + 1, right - left + 1)
            else:
                sortedCounter = sorted(counter.items(), key=lambda x: x[1])
                if sum(map(lambda x: x[1], sortedCounter[:-1])) <= k:
                    ans = max(ans, right - left + 1)
                else:
                    counter[s[left]] -= 1
                    left += 1
            right += 1
        return ans





solution = Solution()
print(solution.characterReplacement("AAAA", 2))