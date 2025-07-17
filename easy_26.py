from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        checked = []

        for i, item in enumerate(nums):
            if item in checked:
                nums[i] = 1000
            else:
                checked.append(item)
        nums.sort()
        return len([num for num in nums if num != 1000])