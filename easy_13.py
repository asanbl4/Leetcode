class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = 0
        n = len(s)
        for i, c in enumerate(s):
            if c == "I" and i != n - 1:
                if s[i + 1] == "V" or s[i + 1] == "X":
                    # print("4 or 9", c, i)
                    ans -= 2
            if c == "X" and i != n - 1:
                if s[i + 1] == "L" or s[i + 1] == "C":
                    # print("40 or 90", c, i)
                    ans -= 20
            if c == "C" and i != n - 1:
                if s[i + 1] == "D" or s[i + 1] == "M":
                    # print("400 or 900", c, i)
                    ans -= 200
            ans += d[c]
        return ans


if __name__ == '__main__':
    s = "MCMXCIV"
    print(Solution().romanToInt(s))