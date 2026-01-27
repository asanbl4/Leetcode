from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(cur, target, nums, subs):
            for num in nums:
                # print(num, cur, subs)
                if cur + num < target:
                    backtrack(cur + num, target, nums, [*subs, num])
                elif cur + num == target:
                    if sorted([*subs, num]) not in ans:
                        ans.append(sorted([*subs, num]))
        backtrack(0, target, nums, [])
        return ans


solution = Solution()
nums=[8,7,4,3]
target=11
print(solution.combinationSum(nums, target))