from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        # Rows & columns
        for i in range(n):
            row_set = set()
            column_set = set()
            for j in range(n):
                if board[i][j].isnumeric() and board[i][j] in row_set:
                    return False
                if board[j][i].isnumeric() and board[j][i] in column_set:
                    return False
                row_set.add(board[i][j])
                column_set.add(board[j][i])

        # 3x3
        for i in range(3):
            for j in range(3):
                row, col = i * 3, j * 3
                s = set()
                for k in range(3):
                    for t in range(3):
                        if board[row + k][col + t].isnumeric() and board[row + k][col + t] in s:
                            return False
                        s.add(board[row + k][col + t])

        return True




if __name__ == '__main__':
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().isValidSudoku(board))