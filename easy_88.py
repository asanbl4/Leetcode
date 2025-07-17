from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()
        print(nums1)


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 4, 0, 0, 0]
    m = 4
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1=nums1, m=m, nums2=nums2, n=n)
