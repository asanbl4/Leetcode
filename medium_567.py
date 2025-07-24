from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        first_d = defaultdict(lambda: 0)
        second_d = defaultdict(lambda: 0)
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            first_d[s1[i]] += 1
            second_d[s2[i]] += 1
        try:
            while right < len(s2):
                # print(sorted(first_d.items()), sorted(filter(lambda x: x[1] != 0,second_d.items())))
                if sorted(first_d.items()) == sorted(filter(lambda x: x[1] != 0,second_d.items())):
                    return True
                right += 1
                second_d[s2[right]] += 1
                second_d[s2[left]] -= 1
                left += 1
        except IndexError:
            return False
        return False

solution = Solution()
print(solution.checkInclusion(s1 = "ab", s2 = ""))

