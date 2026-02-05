from typing import List
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        distance = 0
        inf = 2 ** 31 - 1
        while q:
            distance += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (0 <= row < m and 0 <= col < n and grid[row][col] == inf):
                        grid[row][col] = distance
                        q.append((row, col))
solution = Solution()
grid = [
  [0,-1],
  [2147483647,2147483647]
]
print(solution.islandsAndTreasure(grid))

