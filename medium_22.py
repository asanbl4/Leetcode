class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        k = 1
        ans = ['(']
        while k < 2 * n:
            # print(ans)
            size = len(ans)
            for i in range(size):
                if ans[i].count('(') < n and ans[i]+'(' not in ans:
                    ans.append(ans[i] + '(')
            for i in range(size):
                if ans[i].count('(') == ans[i].count(')') and ans[i]+'(' not in ans:
                    ans.append(ans[i] + '(')
                elif ans[i].count('(') > ans[i].count(')') and ans[i]+')' not in ans:
                    ans.append(ans[i] + ')')
            ans = list(filter(lambda x: len(x) == k + 1, ans))
            k += 1
        return sorted(ans)