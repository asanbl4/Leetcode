from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def bfs(i, j):
            nonlocal grid, visited
            if not 0 <= i < m or not 0 <= j < n:
                return
            if visited[i][j]:
                return
            if grid[i][j] == '0':
                return
            visited[i][j] = True
            bfs(i - 1, j)
            bfs(i + 1, j)
            bfs(i, j - 1)
            bfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    ans += 1
        # print(visited)
        return ans

solution = Solution()
print(solution.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

