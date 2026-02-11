class Solution:
    def reverseBits(self, n: int) -> int:
        bits = ''
        ans = 0
        while n:
            bits += str(n % 2)
            n //= 2
        bits += '0'*(32 - len(bits))
        for i in range(len(bits)):
            # print(i, bits[i], len(bits) - i - 1)
            ans += int(bits[i]) * 2 ** (len(bits) - i - 1)
        return ans
solution = Solution()
print(solution.reverseBits(43261596))
