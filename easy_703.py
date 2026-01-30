from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.priority = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        self.priority.append(val)
        self.priority.sort(reverse=True)
        # print(self.priority)
        return self.priority[self.k - 1]


kthLargest = KthLargest(4, [7, 7, 7, 7, 8, 3])
print(kthLargest.add(2))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(9))
