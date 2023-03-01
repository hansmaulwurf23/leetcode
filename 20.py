class Solution:
    def isValid(self, s: str) -> bool:
        inv = {')': '(', '}': '{', ']': '['}
        chunk = []
        for c in s:
            if c in ('(', '{', '['):
                chunk.append(c)
            elif c in inv:
                if chunk and chunk[-1] == inv[c]:
                    chunk.pop()
                else:
                    return False

        return chunk == []


if __name__ == '__main__':
    s = Solution()
    assert s.isValid('()[]{}') is True
    assert s.isValid('()[]}') is False
    assert s.isValid('()[]{') is False
