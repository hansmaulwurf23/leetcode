class Solution:
    def myAtoi(self, s: str) -> int:
        i, slen = 0, len(s)
        while i < slen and s[i] == ' ':
            i += 1

        if i >= slen:
            return 0  # not really specified!

        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        v = []
        while i < slen and ord('0') <= ord(s[i]) <= ord('9'):
            v.append(s[i])
            i += 1

        res = sign * int(''.join(v) if v else '0')
        if res < (l := -pow(2, 31)):
            return l
        if res > (u := pow(2, 31) - 1):
            return u
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.myAtoi('123') == 123
    assert s.myAtoi('42') == 42
    assert s.myAtoi('   42') == 42
    assert s.myAtoi('   42 with words') == 42
    assert s.myAtoi('   ') == 0
    assert s.myAtoi('  + ') == 0