from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def bfs(i, j, area):
            nonlocal grid, visited
            if not 0 <= i < m or not 0 <= j < n:
                return area - 1
            if visited[i][j]:
                return area - 1
            if grid[i][j] == 0:
                return area - 1
            visited[i][j] = True

            return bfs(i - 1, j, area + 1) + bfs(i + 1, j, area + 1) + bfs(i, j - 1, area + 1) + bfs(i, j + 1, area + 1) - 3 * area

        areas = [0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    areas.append(bfs(i, j, 1))
        return max(areas)

solution = Solution()
print(solution.maxAreaOfIsland(grid = [[1,0,1,1,1,0,1]]
))
