class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        opened = []
        for i in range(len(s)):
            if s[i] in opening:
                opened.append(s[i])
            else:
                try:
                    if opening.index(opened[-1]) == closing.index(s[i]):
                        opened.pop(-1)
                    else:
                        return False
                except IndexError: # in case of opened array is empty
                    return False
        if opened:
            return False
        return True


if __name__ == '__main__':
    s = '([{}])'
    print(Solution().isValid(s))