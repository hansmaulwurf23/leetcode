class Solution:
    def reverse(self, x: int) -> int:
        s = str(x) if x >= 0 else str(x)[1:]
        i = int(''.join(reversed(s))) * (1 if x >= 0 else -1)
        if -pow(2, 31) <= i <= pow(2, 31) - 1:
            return i
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(0) == 0
