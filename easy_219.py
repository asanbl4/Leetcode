from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = nums[:k + 1]
        if sorted(a) != sorted(list(set(a))):
            return True
        for i in range(k + 1, len(nums)):
            a.append(nums[i])
            a.pop(0)
            if a[-1] in a[:-1]:
                return True
        return False


if __name__ == '__main__':
    nums = [13,23,1,2,3]
    k = 5
    print(Solution().containsNearbyDuplicate(nums, k))
