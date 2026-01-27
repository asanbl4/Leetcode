from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur, left, visited):
            visited.append(sorted(cur))
            for num in left:
                if sorted([*cur, num]) not in visited:
                    dfs([*cur, num], [i for i in left if i != num], visited)
            return visited
        return dfs([], nums, [])

solution = Solution()
print(solution.subsets([1,2,3]))