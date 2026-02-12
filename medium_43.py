class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sum = 0
        first = len(num1) - 1
        while first >= 0:
            second = len(num2) - 1
            while second >= 0:
                # print(num1[first], num2[second], (int(num1[first]) * int(num2[second]) * 10 ** (len(num2) - second - 1 + len(num1) - first - 1)))
                sum += (int(num1[first]) * int(num2[second]) * 10 ** (len(num2) - second - 1 + len(num1) - first - 1))
                second -= 1
            first -= 1
        return sum

solution = Solution()
print(solution.multiply("123", "456"))