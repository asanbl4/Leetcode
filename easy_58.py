class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = False
        length = 0
        for i in s[::-1]:
            if i != ' ' and not start:
                start = True
            if start:
                if i == ' ':
                    break
                length += 1
        return length


if __name__ == '__main__':
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))