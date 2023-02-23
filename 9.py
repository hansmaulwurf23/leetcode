class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        lm = len(s) // 2
        for i, (a, b) in enumerate(zip(s, reversed(s))):
            if a != b:
                return False
            elif i > lm:
                return True

        return True