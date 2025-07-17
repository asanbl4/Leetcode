class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        if dividend >= 0:
            if divisor > 0:
                while dividend - divisor >= 0:
                    dividend -= divisor
                    res += 1
            else:
                while dividend + divisor >= 0:
                    dividend += divisor
                    res -= 1
        else:
            if divisor > 0:
                while dividend + divisor <= 0:
                    dividend += divisor
                    res -= 1
            else:
                while dividend - divisor <= 0:
                    dividend -= divisor
                    res += 1

        return res

solution = Solution()
print(solution.divide(7, -3))

