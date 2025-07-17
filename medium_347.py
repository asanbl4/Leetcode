from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = defaultdict(lambda: 0)
        for n in nums:
            d[n] += 1
        return list(map(lambda x: x[0], list(sorted(list(d.items()), key=lambda x: x[1], reverse=True)[:k])))

solution = Solution()
print(solution.topKFrequent([1], 1))