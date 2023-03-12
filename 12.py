class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L',
                  40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = []
        for n, r in romans.items():
            a, b = divmod(num, n)
            res.append(r * a)
            num = b
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    assert (x := s.intToRoman(3)) == 'III', f'got {x}'
    assert (x := s.intToRoman(4)) == 'IV', f'got {x}'
    assert (x := s.intToRoman(12)) == 'XII', f'got {x}'
    assert (x := s.intToRoman(501)) == 'DI', f'got {x}'
    assert (x := s.intToRoman(1994)) == 'MCMXCIV', f'got {x}'