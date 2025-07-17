# UNFINISHED

class Solution:
    def calculate(self, s: str) -> int:
        stk = [i for i in s if i != ' ']
        res = 0
        idx = 0
        previous_operation = None
        operations = ["+", "-"]
        while idx < len(stk):
            print(stk)
            if stk[idx] == '(':
                # find nested paranthesis
                opened, closed = 1, 0
                end = -1
                for i in range(1, len(stk)):
                    if stk[i] == '(':
                        opened += 1
                    elif stk[i] == ')':
                        closed += 1
                    if opened == closed:
                        end = i
                        break
                # recursive parentheses calculation
                res += self.calculate(''.join(stk[1: end]))

                break
                idx = end
            elif stk[idx].isnumeric():
                if previous_operation == "-":
                    res -= int(stk[idx])
                else:
                    res += int(stk[idx])
            elif stk[idx] in operations:
                previous_operation = stk[idx]
            idx += 1
        return res



if __name__ == '__main__':
    s="-(2+1)"
    print(Solution().calculate(s))