class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == '__main__':
    haystack = "leetcode"
    needle = "eet"
    print(Solution().strStr(haystack, needle))