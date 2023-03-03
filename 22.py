from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(left, stack, prefix):
            res = []
            if left > 0:
                if stack:
                    res.extend(gen(left, stack - 1, prefix + ')'))
                res.extend(gen(left - 1, stack + 1, prefix + '('))
            else:
                while stack:
                    prefix += ')'
                    stack -= 1
                res = [prefix]
            return res

        return gen(n, 0, '')



if __name__ == '__main__':
    s = Solution()
    test_cases = [
        (3, ["((()))","(()())","(())()","()(())","()()()"])
    ]

    for n, r in test_cases:
        got = sorted(s.generateParenthesis(n))
        if sorted(r) != got:
            print(f'WRONG got {got} expectec {r}')