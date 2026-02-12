from pkgutil import resolve_name
from typing import List
from collections import deque

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, column = 0, 0
        trueZeros = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    trueZeros.append((i, j))
        while trueZeros:
            r, c = trueZeros.popleft()
            for i in range(n):
                matrix[r][i] = 0
            for i in range(m):
                matrix[i][c] = 0
        for i in matrix:
            print(i)
matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution = Solution()
print(solution.setZeroes(matrix))
