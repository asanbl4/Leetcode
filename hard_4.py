class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        if len(merged) % 2:
            return merged[len(merged) // 2]
        return (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2