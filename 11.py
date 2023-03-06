import datetime
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lv, rv = height[l], height[r]
        max_area = min(lv, rv) * r
        while l < r:
            if lv < rv:
                l += 1
            else:
                r -= 1
            if height[l] <= lv and height[r] <= rv:
                continue
            lv, rv = height[l], height[r]
            area = (r - l) * min(lv, rv)
            if area > max_area:
                max_area = area

        return max_area


if __name__ == '__main__':
    begin = datetime.datetime.now()
    s = Solution()
    assert (x := s.maxArea([1,8,6,2,5,4,8,3,7])) == 49, f'got {x}'
    assert (x := s.maxArea([1,2,1])) == 2, f'got {x}'
    assert (x := s.maxArea(list(range(10000)) + list(range(10000, 0, -1)))) == 50000000, f'got {x}'
    print(f'{datetime.datetime.now() - begin}')
