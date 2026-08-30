from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_i = nums.index(min(nums))
        max_i = nums.index(max(nums))

        left = min(min_i, max_i)
        right = max(min_i, max_i)

        return min(
            right + 1,
            n - left,
            left + 1 + n - right
        )