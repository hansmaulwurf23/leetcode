from itertools import takewhile


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.rest_match(s, self.simplify_pattern(self.split_pattern(p)), 0, 0)

    def split_pattern(self, p: str) -> list:
        pi = 0
        elems = []
        while pi < len(p):
            c = p[pi]
            if pi + 1 < len(p) and p[pi+1] == '*':
                elems.append((c, True))
                pi += 2
            else:
                elems.append((c, False))
                pi += 1
        return elems

    def simplify_pattern(self, p: list) -> list:
        res = [p[0]]
        pi = 1
        while pi < len(p):
            (pc, pr), (lpc, lpr) = p[pi], res[-1]
            # at least one of the pattern elements does not repeat (*)
            if not (lpr and pr):
                res.append(p[pi])
            # both repeat
            elif lpc != pc:
                if pc == '.':
                    # replace pattern character with . since its more generic
                    res[-1][0] = pc
                else:
                    res.append(p[pi])
            pi += 1
        print(f'simplified {self.tup2str(p)} to {self.tup2str(res)}')
        return res

    def tup2str(self, p: list) -> str:
        return "".join(map(lambda x: x[0] + ("*" if x[1] else ""), p))

    def rest_match(self, s: str, pattern: list, si: int, pi: int) -> bool:
        #print(f'{s[si:]} ==~ {"".join(map(lambda x: x[0] + "*" if x[1] else "", pattern[pi:]))}')
        # string already complete
        if si >= len(s):
            if pi < len(pattern):
                # pattern is repeat -> optional -> could still be a match
                if pattern[pi][1]:
                    return self.rest_match(s, pattern, si, pi+1)
                else:
                    return False
            else:
                return True

        # pattern already complete
        if pi >= len(pattern):
            # string cannot be complete since this is handled above
            return False

        pc, repeat = pattern[pi]
        if repeat:
            return any([self.rest_match(s, pattern, i+1, pi+1) for i in
                        takewhile(lambda i: i == si-1 or i >= len(s) or s[i] == pc or pc == '.', range(si-1, len(s)+1))])
        else:
            if pc == '.' or pc == s[si]:
                return self.rest_match(s, pattern, si+1, pi+1)
            else:
                return False
    

if __name__ == '__main__':
    sol = Solution()
    test_cases = [
        ('aa', 'a', False),
        ('aa', 'a*', True),
        ('aaa', 'a*a', True),
        ('ab', '.*', True),
        ('ab', '.*..c*', True),
        ('a', 'ab*a', False),
        ('aaab', 'a*', False),
        ('aaab', 'a*b', True),
        ('aaab', 'c*a*b*', True),
        ('bbbba', '.*a*a', True),
        ('aaa', 'ab*a*c*a', True),
        ('aaaaaaaaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*', False),
    ]

    for s, p, r in test_cases:
        x = sol.isMatch(s, p)
        if x != r:
            assert False, f'matching {s} with {p} got {x} expected {r}'
