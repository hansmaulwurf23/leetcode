class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        maxl = 1
        used = set(s[0])
        for i, c in enumerate(s[1:], 1):
            if c in used:
                n = s.find(c, l)
                if n - l > 0:
                    used -= set(s[l:n])
                l = n + 1
            else:
                used.add(c)
            if i - l + 1 > maxl:
                maxl = i - l + 1

        return maxl


if __name__ == '__main__':
    s = Solution()
    assert (x := s.lengthOfLongestSubstring('abcdefgahijk')) == 11, f'got {x}'
    assert (x := s.lengthOfLongestSubstring('abcabcbb')) == 3, f'got {x}'
    assert (x := s.lengthOfLongestSubstring('bbbbb')) == 1, f'got {x}'
    assert (x := s.lengthOfLongestSubstring('pwwkew')) == 3, f'got {x}'
    assert (x := s.lengthOfLongestSubstring(' ')) == 1, f'got {x}'
