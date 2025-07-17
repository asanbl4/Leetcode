class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        d = {}
        for i in nums:
            d[i] = True
        mmax = 0
        for i in range(len(nums)):
            el = nums[i]
            if not el-1 in d.keys():
                streak = 1
                while el+1 in d.keys():
                    streak += 1
                    el += 1
                mmax = max(mmax, streak)
        return mmax


if __name__ == '__main__':
    nums =[0,3,7,2,5,8,4,6,0,1]
    print(Solution().longestConsecutive(nums))