class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        mmax = 0
        for r in range(len(s)):
            if s[r] not in chars:
                chars.add(s[r])
                mmax = max(mmax, r - l + 1)
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
                chars.add(s[r])
        return mmax



if __name__ == '__main__':
    s = ""
    print(Solution().lengthOfLongestSubstring(s))