from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': ('a','b','c'),
            '3': ('d','e','f'),
            '4': ('g','h','i'),
            '5': ('j','k','l'),
            '6': ('m','n','o'),
            '7': ('p','q','r','s'),
            '8': ('t','u','v'),
            '9': ('w','x','y','z'),
        }

        if not digits:
            return []

        res = list(m[digits[0]])
        for d in digits[1:]:
            new_res = []
            chars = m[d]
            for r in res:
                for c in chars:
                    new_res.append(f'{r}{c}')
            res = new_res
        return res


if __name__ == '__main__':
    s = Solution()
    test_cases = [
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a","b","c"])
    ]

    for inp, res in test_cases:
        r = s.letterCombinations(inp)
        if set(r) != set(res):
            assert False, f'got {r} expected {res}'
