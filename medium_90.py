from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur, left, visited):
            visited.append(sorted(cur))
            for num in left:
                copy_left = left.copy()
                if sorted([*cur, num]) not in visited:
                    copy_left.remove(num)
                    dfs([*cur, num], copy_left, visited)
            return visited
        return dfs([], nums, [])


solution = Solution()
nums = [7,7]
print(solution.subsetsWithDup(nums))