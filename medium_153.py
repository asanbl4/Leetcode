class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        minn = 5001
        while l <= r:
            mid = (l + r) // 2
            # print(l, r, mid, "\t", nums[mid], nums[l])
            minn = min(minn, nums[l])
            if nums[mid] < nums[l]: # rotated > len // 2 times, min is there
                r = mid
            else: # rotated <= len // 2, min is there
                l = mid + 1
        return minn

solution = Solution()
print(solution.findMin(nums = [1]))

