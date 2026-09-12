from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        intervals = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        @lru_cache(None)
        def dp(i, k):
            if i == len(intervals) or k == 0:
                return (0, ())

            # Don't choose current interval
            skip = dp(i + 1, k)

            l, r, w, idx = intervals[i]

            # First interval whose start > current end
            j = bisect_right(
                intervals,
                (r, float('inf'), float('inf'), float('inf'))
            )

            next_weight, next_indices = dp(j, k - 1)

            take = (
                w + next_weight,
                tuple(sorted((idx,) + next_indices))
            )

            if take[0] > skip[0]:
                return take

            if take[0] < skip[0]:
                return skip

            return min(take, skip)

        return list(dp(0, 4)[1])