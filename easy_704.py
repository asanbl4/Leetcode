class Solution:
    def search(self, nums: list[int], target: int) -> int:
        ans = -1
        m, n = 0, len(nums) - 1

        while m <= n:
            mid = (m + n) // 2
            if nums[mid] == target:
                ans = mid
                break
            elif nums[mid] < target:
                m = mid + 1
            else:
                n = mid - 1
        return ans

