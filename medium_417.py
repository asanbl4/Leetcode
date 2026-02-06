from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j, visited: set):
            visited.add((i, j))
            q = deque()
            for di, dj in directions:
                row = i + di
                col = j + dj
                if 0 <= row < m and 0 <= col < n and not (row, col) in visited:
                    print((i, j), (row, col))
                    if heights[row][col] >= heights[i][j]:
                        q.append((row, col))
            while q:
                i, j = q.popleft()
                visited.update(dfs(i, j, visited))
            return visited

        atlantic = set()
        pacific = set()
        for i in range(m): atlantic.update(dfs(i, 0, atlantic))
        for i in range(n): atlantic.update(dfs(0, i, atlantic))
        for i in range(m): pacific.update(dfs(i, n - 1, pacific))
        for i in range(n): pacific.update(dfs(m - 1, i, pacific))
        return list(pacific &  atlantic)

solution = Solution()
heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]]
print(solution.pacificAtlantic(heights))




