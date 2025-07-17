class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for char in s:
            try:
                d[char] += 1
            except KeyError:
                d[char] = 1
        for char in t:
            try:
                d[char] -= 1
            except KeyError:
                return False
        for i in d.values():
            if i != 0:
                return False
        return True


if __name__ == '__main__':
    s = "rac"
    t = "car"
    print(Solution().isAnagram(s, t))