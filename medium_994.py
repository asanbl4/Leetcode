from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        minutes = 0
        while q and fresh_oranges > 0:
            # print(q)
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in directions:
                    r = i + di
                    c = j + dj
                    # print(r, c)
                    if (0 <= r < m and 0 <= c < n and grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh_oranges -= 1
                        q.append((r,c))
            minutes += 1
        return minutes if fresh_oranges == 0 else -1

solution = Solution()
grid =[[2,1,1],[1,1,0],[0,1,1]]

print(solution.orangesRotting(grid))