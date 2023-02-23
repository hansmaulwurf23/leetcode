from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        snums = sorted(nums)
        l, u = 0, len(nums) - 1
        while l < u:
            s = snums[l] + snums[u]
            if s < target:
                l += 1
            elif s > target:
                u -= 1
            else:
                if snums[l] != snums[u]:
                    return [nums.index(snums[l]), nums.index(snums[u])]
                else:
                    one = nums.index(snums[l])
                    return [one, nums.index(snums[u], one + 1)]