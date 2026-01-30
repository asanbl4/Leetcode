from typing import List
import heapq

class Solution: # no sorting
    def findKthLargest(self, nums: List[int], k: int) -> int:
        initialHeap = nums[:k]
        heapq.heapify(initialHeap)
        for num in nums[k:]:
            if num >= initialHeap[0]:
                heapq.heappop(initialHeap)
                heapq.heappush(initialHeap, num)
        return initialHeap[0]


solution = Solution()
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4))
