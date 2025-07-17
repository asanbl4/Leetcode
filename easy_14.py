from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs)
        for s in strs:
            for i in range(len(s)):
                try:
                    if s[i] != prefix[i]:
                        prefix = prefix[:i]
                except IndexError:
                    pass
        return prefix


if __name__ == '__main__':
    strs = ["cir" , "car"]
    print(Solution().longestCommonPrefix(strs))