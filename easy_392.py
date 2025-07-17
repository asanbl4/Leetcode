class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        if not len(s):
            return True

        for i in range(len(t)):
            try:
                if s[idx] == t[i]:
                    idx += 1
            except IndexError:
                break
        if idx == len(s):
            return True
        return False


if __name__ == '__main__':
    s = "bb"
    t = "abghdc"
    print(Solution().isSubsequence(s, t))