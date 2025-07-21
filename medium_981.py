from collections import defaultdict

class TimeMap:

    def __init__(self):
        # self.timeMap = defaultdict(lambda: []) # key: {timestamp1: value1, timestamp2: value2}
        self.timeMap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap.keys():
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        value = self.timeMap.get(key, [])
        l = 0
        r = len(value) - 1
        ans = None
        while l <= r:
            mid = (l + r) // 2
            if value[mid][0] <= timestamp:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        if ans is not None:
            return value[ans][1]
        return ""

# Your TimeMap object will be instantiated and called as such:
timeMap = TimeMap()
timeMap.set("love","high",10)
timeMap.set("love","low",20)
print(timeMap.get("love", 5))
print(timeMap.get("love",10))
print(timeMap.get("love",15))
print(timeMap.get("love",20))
print(timeMap.get("love",25))