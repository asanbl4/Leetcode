from typing import List, Counter
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.counter = Counter()
        self.dots = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.counter[x, y] += 1
        self.dots[x].add(y)

    def count(self, point: List[int]) -> int:
        x, y = point

        for yy in self.dots[x]:
            sideLength = yy - y
            ans +=

detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])
detectSquares.count([11, 10])
detectSquares.count([14, 8])
detectSquares.add([11, 2])
detectSquares.count([11, 10])