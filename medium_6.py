class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        idx, d = 0, 1
        for char in s:
            rows[idx].append(char)
            if idx == numRows - 1:
                d = -1
            if idx == 0:
                d = 1
            idx += d

        return ''.join(map(lambda x: ''.join(x), rows))


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))