class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        for i in range(len(temperatures) - 1):
            stack.append(temperatures[i + 1] - temperatures[i])
            if stack[i] > 1:
                stack[i] = 1
        stack.append(0)
        return stack


solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# print(solution.dailyTemperatures([30, 40, 50, 60]))