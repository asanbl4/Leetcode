from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        maxRadius = n // 2
        print(maxRadius)
        if maxRadius > 0:
            for circle in range(1, maxRadius + 1):
                for i in range(circle - 1, n - circle):
                    # print("first:", circle - 1, i)
                    # print("second:", i, n - circle)
                    # print("third:", n - circle, n - i - 1)
                    # print("fourth:", n - i - 1, circle - 1)
                    firstVal = matrix[circle - 1][i]
                    secondVal = matrix[i][n - circle]
                    thirdVal = matrix[n - circle][n - i - 1]
                    fourthVal = matrix[n - i - 1][circle - 1]
                    matrix[circle - 1][i] = fourthVal
                    matrix[i][n - circle] = firstVal
                    matrix[n - circle][n - i - 1] = secondVal
                    matrix[n - i - 1][circle - 1] = thirdVal
                    # matrix[circle - 1][circle - 1 + i] -> matrix[circle - 1 + i][n - circle]
                    # matrix[circle - 1 + i][n - circle] -> matrix[n - circle][n - circle - i],
                    # matrix[n - circle][n - circle - i] -> matrix[n - circle - i][circle - 1],
                    # matrix[n - circle - i][circle - 1] -> matrix[circle - 1][circle - 1 + i]
        # for i in matrix:
        #     print(i)
# matrix = [[5, 1, 9, 11],
#           [2, 4, 8, 10],
#           [13, 3, 6, 7],
#           [15, 14, 12, 16]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
#

matrix = [[2,29,20,26,16,28],
          [12,27,9,25,13,21],
          [32,33,32,2,28,14],
          [13,14,32,27,22,26],
          [33,1,20,7,21,7],
          [4,24,1,6,32,34]]
solution = Solution()
print(solution.rotate(matrix))