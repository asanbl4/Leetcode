from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = [[False] * n for _ in range(m)]

        def dfs_collect(sr: int, sc: int):
            stack = [(sr, sc)]
            visited[sr][sc] = True
            cells = [(sr, sc)]
            touches_border = (sr == 0 or sr == m - 1 or sc == 0 or sc == n - 1)

            while stack:
                r, c = stack.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and board[nr][nc] == 'O':
                        visited[nr][nc] = True
                        stack.append((nr, nc))
                        cells.append((nr, nc))
                        if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                            touches_border = True

            return cells, touches_border

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    cells, touches_border = dfs_collect(i, j)
                    if not touches_border:
                        for r, c in cells:
                            board[r][c] = 'X'
solution = Solution()
board =[["O","O","O","O","X","X"],
        ["O","O","O","O","O","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","X","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","O","O"]]
print(solution.solve(board))