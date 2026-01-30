import heapq
from typing import Optional


class MedianFinder:

    def __init__(self):
        self.leftHeap = [] # inverted minHeap (maxHeap)
        self.rightHeap = []

    def addNum(self, num: int) -> None:

        if len(self.leftHeap) == len(self.rightHeap):
            # push the new val to leftHeap; push the min val of leftHeap inversed to rightHeap and pop it from leftHeap
            heapq.heappush(self.rightHeap, -heapq.heappushpop(self.leftHeap, -num))
        else:
            # push the new val to rightHeap; push the min val of rightHeap inversed to leftHeap and pop it from rightHeap
            # print(self.leftHeap, self.rightHeap, num)
            heapq.heappush(self.leftHeap, -heapq.heappushpop(self.rightHeap, num))

    def findMedian(self) -> float:
        # print(self.leftHeap, self.rightHeap)
        if len(self.leftHeap) == len(self.rightHeap):
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2
        return self.rightHeap[0]


medianFinder = MedianFinder()
medianFinder.addNum(-1)
print(medianFinder.findMedian())
medianFinder.addNum(-2)
print(medianFinder.findMedian())
medianFinder.addNum(-3)
print(medianFinder.findMedian())
medianFinder.addNum(-4)
print(medianFinder.findMedian())
medianFinder.addNum(-5)
print(medianFinder.findMedian())

# medianFinder = MedianFinder()
# medianFinder.addNum(1)
# medianFinder.addNum(2)
# print(medianFinder.findMedian())
# medianFinder.addNum(3)
# print(medianFinder.findMedian())