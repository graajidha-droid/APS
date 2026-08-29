from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pairs = sorted((num, i) for i, num in enumerate(nums))
        ans = [0] * len(nums)

        start = 0

        for end in range(1, len(nums) + 1):
            if end == len(nums) or pairs[end][0] - pairs[end - 1][0] > limit:
                values = sorted(pairs[i][0] for i in range(start, end))
                indices = sorted(pairs[i][1] for i in range(start, end))

                for index, value in zip(indices, values):
                    ans[index] = value

                start = end

        return ans