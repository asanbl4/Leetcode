from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 2):
            if nums[i] == nums[i + 1] == nums[i + 2]:
                nums.pop(i)
                nums.insert(0, int(1e9))
            # print(nums)
        nums.sort()
        # print(nums)
        return len([num for num in nums if num != 1e9])