from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] <= prev[1]:
                prev[1] = max(prev[1], cur[1])
            else:
                ans.append(prev)
                prev = cur
        ans.append(prev)
        return ans
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)