class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphastring = ''.join([c.lower() for c in s if c.isalpha() or c.isnumeric()])
        l = 0
        r = len(alphastring) - 1
        while l < r:
            if alphastring[l] != alphastring[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == '__main__':
    s = "a"
    print(Solution().isPalindrome(s))