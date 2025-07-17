from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        cur = []

        def combination(start: int):
            if len(cur) == k:
                ans.append(cur[:])
                return
            for i in range(start, n + 1):
                cur.append(i)
                combination(i + 1)
                cur.pop()

        combination(1)
        return ans

print(Solution().combine(4, 2))