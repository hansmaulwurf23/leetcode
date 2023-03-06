class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        si, pi = 0, 0   # string index and pattern index

        # if pattern contains repeats but ends with non-repeats, we remove the non repeat part first
        if (li := p.rfind('*')) >= 0 and li < len(p) - 1:
            end_pattern = p[li+1:]
            # match from the back of the pattern and the back of the string, and remove from s and p
            for pc in reversed(end_pattern):
                if s[-1] != pc and pc != '.':
                    return False
                s = s[:len(s)-1]
            p = p[:li+1]

        while pi < len(p) and si < len(s):
            # pc is the pattern character we are currently looking for (can be '.')
            pc = p[pi]
            repeat = False
            if pi + 1 < len(p) and p[pi + 1] == '*':
                repeat = True
                pi += 1

            if repeat:
                # 'terminating character' of the repeating struct, ie a*b -> b is tc
                tc = None
                if len(p) > pi + 1 and not (len(p) > pi + 2 and p[pi+2] == '*'):
                    tc = p[pi+1]

                if pc == '.':
                    if tc is not None:
                        while si < len(s) and s[si] != tc:
                            si += 1
                    else:
                        while si < len(s):
                            si += 1
                else:
                    min_occs = 0
                    # if tc is the pc, structs like a*aaa means we need to match at least 3 a's
                    while pc == tc:
                        min_occs += 1
                        if pi + 1 >= len(p) or p[pi + 1] != tc:
                            break
                        pi += 1

                    while si < len(s) and pc == s[si]:
                        si += 1
                        if min_occs > 0:
                            min_occs -= 1
                    if min_occs:
                        return False
                pi += 1
            else:
                if s[si] != pc and pc != '.':
                    return False
                else:
                    si += 1
                    pi += 1

        # if smth left of pattern, check if it is only optionals
        while pi + 1 < len(p):
            if p[pi+1] == '*':
                pi += 2
            else:
                return False

        return pi >= len(p) and si >= len(s)


if __name__ == '__main__':
    s = Solution()
    assert s.isMatch('aa', 'a') is False
    assert s.isMatch('aa', 'a*') is True
    assert s.isMatch('aaa', 'a*a') is True
    assert s.isMatch('ab', '.*') is True
    assert s.isMatch('ab', '.*..c*') is True
    assert s.isMatch('a', 'ab*a') is False
    assert s.isMatch('aaab', 'a*') is False
    assert s.isMatch('aaab', 'a*b') is True
    assert s.isMatch('aaab', 'c*a*b*') is True
    assert s.isMatch('bbbba', '.*a*a') is True
    assert s.isMatch('aaa', 'ab*a*c*a') is True
