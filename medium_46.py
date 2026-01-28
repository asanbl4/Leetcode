from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(cur, left):
            if not left and cur not in ans:
                ans.append(cur)
                return
            for num in left:
                if num not in cur:
                    # print([*cur, num], [i for i in left if i != num])
                    backtrack([*cur, num], [i for i in left if i != num])
        backtrack([], nums)
        return ans

solution = Solution()
print(solution.permute([7]))