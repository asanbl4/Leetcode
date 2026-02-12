from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newNumber = []
        i = len(digits) - 1
        if digits[-1] == 9:
            while digits[i] == 9 and i >= 0:
                newNumber.append(0)
                i -= 1
        if i == -1:
            return[1, *newNumber]
        return [*digits[:i], digits[i] + 1, *newNumber[::-1]]
solution = Solution()
print(solution.plusOne([9,9,9]))