from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop(-1)


if __name__ == '__main__':
    s = Solution()
    nums = [-1,-100,3,99]
    s.rotate(nums, 2)