class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        opposite, even = 1, 0
        if nums[0] % 2 == 0:
            even = 1
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                even += 1
            if nums[i] % 2 != nums[i - 1] % 2:
                opposite += 1
        return max(opposite, even, len(nums) - even)

solution = Solution()
print(solution.maximumLength([1, 2, 1, 2, 1, 2]))
