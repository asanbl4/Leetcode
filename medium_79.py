from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(i, j, substring):
            if not substring:
                return True
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]):
                return False
            if used[i][j]:
                return False
            if board[i][j] != substring[0]:
                return False
            used[i][j] = True
            ans = (dfs(i - 1, j, substring[1:]) or
                   dfs(i + 1, j, substring[1:]) or
                   dfs(i, j - 1, substring[1:]) or
                   dfs(i, j + 1, substring[1:]))
            used[i][j] = False
            return ans

        for ii in range(len(board)):
            for jj in range(len(board[0])):
                res = dfs(ii, jj, word)
                if res:
                    return True
        return False




solution = Solution()
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]]
word = "ABCCED"
print(solution.exist(board, word))
