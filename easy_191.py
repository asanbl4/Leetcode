class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # print(n)
            count += n % 2
            n //= 2
        return count

solution = Solution()
# print(solution.hammingWeight(11))