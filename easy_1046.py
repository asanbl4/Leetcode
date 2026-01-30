from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        x, y = stones[-2], stones[-1]
        stones = stones[:-2]
        if x != y:
            stones.append(y - x)
        return self.lastStoneWeight(stones)


solution = Solution()
print(solution.lastStoneWeight(stones = [2,2]))
