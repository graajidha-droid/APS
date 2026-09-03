from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        min_odd = float("inf")
        has_odd = False
        has_even = False

        for num in nums1:
            if num % 2:
                has_odd = True
                min_odd = min(min_odd, num)
            else:
                has_even = True

        if not has_odd or not has_even:
            return True

        for num in nums1:
            if num % 2 == 0 and num < min_odd:
                return False

        return True