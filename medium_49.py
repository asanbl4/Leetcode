from typing import List


class Solution:
    def strToDict(self, s: str) -> dict[str:int]:
        d = {}
        for char in s:
            try:
                d[char] += 1
            except KeyError:
                d[char] = 1
        return tuple(sorted(d.items()))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            temp_d = self.strToDict(strs[i])
            if temp_d not in d.keys():
                d[temp_d] = [strs[i]]
            else:
                d[temp_d].append(strs[i])
        # print(d)
        return list(d.values())

if __name__ == '__main__':
    strs = ["abc", 'cba', 'c', 'cd']
    print(Solution().groupAnagrams(strs))


