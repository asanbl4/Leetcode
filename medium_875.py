import math
from collections import defaultdict


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = defaultdict(lambda: r)
        while l < r:
            mid = (l + r) // 2
            hours = sum(map(lambda x: math.ceil(x / mid), piles))
            print(l, r, mid, hours)
            if hours <= h: # too fast, decrease mid (speed)
                ans[h] = min(ans[h], mid)
                r = mid
            elif hours > h: # too slow, increase mid (speed)
                l = mid + 1
            # else:
                # l += 1
        return ans.get(h, max(piles))


solution = Solution()
print(solution.minEatingSpeed(piles = [312884470], h = 312884469))