class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d.keys():
                d[s[i]] = t[i]

        seen_values = set()
        unique_dict = {}

        for key, value in d.items():
            if value not in seen_values:
                unique_dict[key] = value
                seen_values.add(value)
        for i in range(len(s)):
            try:
                if unique_dict[s[i]] != t[i]:
                    return False
            except KeyError:
                return False
        return True

if __name__ == '__main__':
    s = "ac"
    t = "ab"
    print(Solution().isIsomorphic(s, t))