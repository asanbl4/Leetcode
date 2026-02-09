from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dp = {}
        def hasCycle(start, cur, visited):
            nonlocal dp
            if start == cur or (start, cur) in visited:
                dp[(start, cur)] = True
                return True
            if (start, cur) in dp:
                return dp[(start, cur)]
            visited[(start, cur)] = True
            queue = deque()
            for i, j in prerequisites:
                if i == cur:
                    queue.append(j)
            # print(queue)
            dp[(start, cur)] = False
            while queue:
                newCur = queue.popleft()
                visited_copy = visited.copy()
                # print(start, cur, newCur)
                dp[(start, cur)] = hasCycle(cur, newCur, visited_copy)
                if dp[(start, cur)]:
                    return True
            return dp[(start, cur)]
        for i in prerequisites:
            # print('--------')
            if hasCycle(i[0], i[1], {}):
                return False
        return True



solution = Solution()
numCourses = 3
prerequisites = [[1, 0], [0, 1]]
print(solution.canFinish(numCourses, prerequisites))