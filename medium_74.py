from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # rows
        n = len(matrix[0]) # cols
        l = 0
        r = m - 1
        targetRowIdx = -1
        while l <= r: # find the row
            mid = (l + r) // 2
            # print(matrix[mid][0], target)
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                targetRowIdx = mid
                l = mid + 1
            else:
                return True
        array = matrix[targetRowIdx]
        l = 0
        r = n - 1
        found = False
        while l <= r:
            mid = (l + r) // 2
            if array[mid] == target:
                found = True
                break
            if array[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return found



if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(Solution().searchMatrix(matrix, target))
