class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].strip('-').isdigit():
                stack.append(tokens[i])
            elif tokens[i] == '+':
                stack.append(int(int(stack.pop()) + int(stack.pop())))
            elif tokens[i] == '*':
                stack.append(int(int(stack.pop()) * int(stack.pop())))
            elif tokens[i] == '-':
                last, prelast = int(stack.pop()), int(stack.pop())
                stack.append(int(prelast - last))
            elif tokens[i] == '/':
                last, prelast = int(stack.pop()), int(stack.pop())
                stack.append(int(prelast / last))
        return int(stack[0])

solution = Solution()
print(solution.evalRPN(["1"]))

