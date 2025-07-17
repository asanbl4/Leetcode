class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        print(self.lis(nums))
    @staticmethod
    def lis(nums):
        l = [1] * len(nums)
        for i in range(1, len(l)):
            l[i] = 1 + max([l[j] for j in range(i) if nums[j] < nums[i]], default=0)
        return max(l)

solution = Solution()
print(solution.lis([10,9,2,5,3,7,101,18]))