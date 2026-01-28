from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(cur, tgt, left, subs):
            copy_left: list = left.copy()
            for num in left:
                # print(num, cur, subs)
                if cur + num < tgt:
                    copy_left.remove(num)
                    backtrack(cur + num, tgt, copy_left, [*subs, num])
                elif cur + num == tgt:
                    if sorted([*subs, num]) not in ans:
                        ans.append(sorted([*subs, num]))

        backtrack(0, target, candidates, [])
        return ans

candidates = [1,1,3,4,5]
target = 7
solution = Solution()
print(solution.combinationSum2(candidates,target))