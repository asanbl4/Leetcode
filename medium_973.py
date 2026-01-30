from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point: List[int]):
            return (point[0] ** 2 + point[1] ** 2) ** (1/2)
        points.sort(key=lambda x: distance(x))
        return points[:k]

solution = Solution()
print(solution.kClosest([[3,3],[5,-1],[-2,4]], k = 2))