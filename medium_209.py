from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 1
        mmin = 1e9
        if len(nums) > 1:
            cur_sum = nums[l] + nums[r]
        else:
            cur_sum = nums[l]
        if nums[l] >= target:
            return 1
        while r < len(nums):
            if cur_sum >= target:
                mmin = min(mmin, r - l + 1)
                cur_sum -= nums[l]
                l += 1
            else:
                r += 1
                try:
                    cur_sum += nums[r]
                except IndexError:
                    break
        return mmin if mmin != 1e9 else 0


if __name__ == '__main__':
    target = 6
    nums = [10,4,4]
    print(Solution().minSubArrayLen(target,nums))