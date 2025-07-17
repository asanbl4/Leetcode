class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        d = {}
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in d.keys():
                d[pattern[i]] = words[i]
            else:
                if not d[pattern[i]] == words[i]:
                    return False
        if len(set(pattern)) != len(set(words)):
            return False
        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog dog dog dog"
    print(Solution().wordPattern(pattern, s))