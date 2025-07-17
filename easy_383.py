class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for char in ransomNote:
            try:
                d[char] += 1
            except KeyError:
                d[char] = 1
        for char in magazine:
            try:
                d[char] -= 1
            except KeyError:
                pass
        for i in d.values():
            if i > 0:
                return False
        return True

if __name__ == '__main__':
    ransomNote = "aassct"
    magazine = "aab"
    print(Solution().canConstruct(ransomNote, magazine))