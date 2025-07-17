from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for i, num in enumerate(nums):
            if num == val:
                k -= 1
                nums[i] = 1000
        nums.sort()
        return k