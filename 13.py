class Solution:
    def romanToInt(self, s: str) -> int:
        syms = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val = 0
        for i, c in enumerate(s):
            val += syms[c]
            if i > 0 and syms[s[i-1]] < syms[c]:
                val -= (2 * syms[s[i-1]])

        return val


if __name__ == '__main__':
    s = Solution()
    assert (x := s.romanToInt('III')) == 3, f'got {x}'
    assert (x := s.romanToInt('C')) == 100, f'got {x}'
    assert (x := s.romanToInt('MDCC')) == 1700, f'got {x}'
    assert (x := s.romanToInt('IV')) == 4, f'got {x}'
    assert (x := s.romanToInt('CM')) == 900, f'got {x}'
    assert (x := s.romanToInt('CD')) == 400, f'got {x}'

