from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        mlen = len(A) + len(B)         # len of merged arrays
        midx = mlen // 2 - 1           # index of median in merged arrays
        ma = (len(A) - 1) // 2
        while True:
            mb = midx - ma - 1
            lpa = A[ma] if ma >= 0 else float('-infinity')
            rpa = A[ma+1] if (ma+1) < len(A) else float('infinity')
            lpb = B[mb] if mb >= 0 else float('-infinity')
            rpb = B[mb+1] if (mb+1) < len(B) else float('infinity')

            if lpa <= rpb and lpb <= rpa:
                if mlen % 2:
                    return min(rpa, rpb)
                else:
                    return (max(lpa, lpb) + min(rpa, rpb)) / 2
            elif lpa > rpb:
                ma -= 1
            else:
                ma += 1



if __name__ == '__main__':
    s = Solution()
    test_cases = [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8], 4),
        ([1, 2, 6, 8, 9], [3, 4, 5, 7], 5.0),
        ([1, 2], [3, 4], 2.5),
        ([1, 3], [2], 2.0),
    ]
    for a, b, r in test_cases:
        x = s.findMedianSortedArrays(a, b)
        if x != r:
            assert False, f'expected {r} for a {a} and b {b} but got {x} instead'
