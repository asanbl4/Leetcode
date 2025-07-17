from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] < candies[i + 1] + 1:
                candies[i] = candies[i + 1] + 1

        print(candies)
        return sum(candies)

if __name__ == '__main__':
    ratings = [1,3,4,5,2]
    print(Solution().candy(ratings))

