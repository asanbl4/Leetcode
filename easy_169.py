from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        elements = {}
        for i in range(n):
            try:
                elements[nums[i]] += 1
            except KeyError:
                elements[nums[i]] = 1
        for key, val in elements.items():
            if val > n // 2:
                return key


if __name__ == '__main__':
    s = Solution()
    nums = [2,2,1,1,1,2,2]
    print(s.majorityElement(nums))