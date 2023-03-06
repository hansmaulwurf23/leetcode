class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        res, i = [], 0
        # 1st row
        while i < len(s):
            res.append(s[i])
            i += (2 * numRows) - 2
        # 2nd to 2nd to last row
        for r in range(1, numRows - 1):
            i = r
            while i < len(s):
                res.append(s[i])
                i += 2 * (numRows - r - 1)
                if i < len(s):
                    res.append(s[i])
                    i += 2 * r
        # last row
        i = numRows - 1
        while i < len(s):
            res.append(s[i])
            i += (2 * numRows) - 2

        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    assert s.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert s.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'

# [1]           [2n-1]             [4n-3]
# [2]       [..] [2n]          [3n+2]  [4n-2]
# [3]     [..]   [2n+1]      [3n+1]    [4n-1]
# [.]   [n+2]    [..]      [3n]        [.]
# [.] [n+1]      [..]    [3n-1]        [.]
# [n]            [3n-2]                [4n+2]
#