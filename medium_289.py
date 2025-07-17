from typing import List


class Solution:
    def countNeighbours(self, i: int, j: int, board: List[List[int]]) -> int:
        sum_neighbours = 0
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in neighbours:
            ni, nj = i + dx, j + dy
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                sum_neighbours += board[ni][nj]
        return sum_neighbours


    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        # changed = [[False] * n] * m
        result = []
        for i in range(m):
            for j in range(n):
                neighbours = self.countNeighbours(i, j, board)
                # print(i, j, neighbours)
                if board[i][j] == 0:
                    print("dead", neighbours, neighbours == 3)
                    result.append(neighbours == 3)
                else:
                    print("live", neighbours, not 2 <= neighbours <= 3)
                    result.append(not 2 <= neighbours <= 3)
        for i in range(m):
            for j in range(n):
                # print(n * i + j)
                if result[n * i + j]:
                    board[i][j] = int(not bool(board[i][j]))
        # print(board)


if __name__ == '__main__':
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Solution().gameOfLife(board)
