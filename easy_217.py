class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return list(dict.fromkeys(nums)) != nums