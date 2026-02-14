from typing import List
from collections import deque

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def dfs(matrix, idx, res):
            if idx == 3:
                if res == target:
                    return True
                return False
            queue = deque(row for row in matrix if row[idx] == target[idx] and row[idx] >= res[idx])
            queue.append(res)
            print(idx, queue)
            while queue:
                curRow = queue.popleft()
                if target[idx] == curRow[idx]:
                    if dfs([row for row in matrix if row != curRow], idx + 1, [max(res[i], curRow[i]) for i in range(3)]):
                        return True
            return False

        return dfs(triplets, 0, [0,0,0])


solution = Solution()
triplets = [[9,4,9],[7,4,8],[10,5,1],[3,7,6],[5,3,4]]
target = [9,7,9]
print(solution.mergeTriplets(triplets, target))



