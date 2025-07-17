class Solution:
    def isHappy(self, n: int) -> bool:
        a = set()
        summ = 0
        s = str(n)
        while summ != 1:
            summ = 0
            for char in s:
                digit = int(char)
                summ += digit ** 2
            s = str(summ)
            if s in a:
                return False
            a.add(s)
        else:
            return True


if __name__ == '__main__':
    n = 2
    print(Solution().isHappy(n))