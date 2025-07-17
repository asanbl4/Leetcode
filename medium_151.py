class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.strip()
        return ' '.join([word for word in s.split()][::-1])

if __name__ == '__main__':
    s = "  the sky is blue"
    print(Solution().reverseWords(s))
