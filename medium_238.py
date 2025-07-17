from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n
        left_product[0] = 1
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        return [left_product[i] * right_product[i] for i in range(n)]




if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # nums = [-1,1,0,-3,3]
    print(Solution().productExceptSelf(nums))