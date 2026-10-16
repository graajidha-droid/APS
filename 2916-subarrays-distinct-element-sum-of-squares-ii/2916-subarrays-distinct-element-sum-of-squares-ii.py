class SegmentTree:

    def __init__(self, n):
        self.n = n
        self.sum = [0] * (4 * n)
        self.sq_sum = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _push(self, node, l, r):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (l + r) // 2

            left_len = mid - l + 1
            self.sq_sum[2 * node] = (
                self.sq_sum[2 * node]
                + 2 * val * self.sum[2 * node]
                + val * val * left_len
            ) % 1000000007
            self.sum[2 * node] = (
                self.sum[2 * node] + val * left_len
            ) % 1000000007
            self.lazy[2 * node] = (self.lazy[2 * node] + val) % 1000000007

            right_len = r - mid
            self.sq_sum[2 * node + 1] = (
                self.sq_sum[2 * node + 1]
                + 2 * val * self.sum[2 * node + 1]
                + val * val * right_len
            ) % 1000000007
            self.sum[2 * node + 1] = (
                self.sum[2 * node + 1] + val * right_len
            ) % 1000000007
            self.lazy[2 * node + 1] = (
                self.lazy[2 * node + 1] + val
            ) % 1000000007

            self.lazy[node] = 0

    def update(self, node, l, r, ql, qr, val):
        if ql <= l and r <= qr:
            length = r - l + 1
            self.sq_sum[node] = (
                self.sq_sum[node] + 2 * val * self.sum[node] + val * val * length
            ) % 1000000007
            self.sum[node] = (self.sum[node] + val * length) % 1000000007
            self.lazy[node] = (self.lazy[node] + val) % 1000000007
            return

        self._push(node, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self.update(2 * node, l, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, r, ql, qr, val)

        self.sum[node] = (self.sum[2 * node] + self.sum[2 * node + 1]) % 1000000007
        self.sq_sum[node] = (
            self.sq_sum[2 * node] + self.sq_sum[2 * node + 1]
        ) % 1000000007


class Solution:

    def sumCounts(self, nums: list[int]) -> int:
        MOD = 1000000007
        n = len(nums)
        tree = SegmentTree(n)
        last_pos = {}
        total_ans = 0

        for i, val in enumerate(nums):
            prev_idx = last_pos.get(val, -1)
            tree.update(1, 0, n - 1, prev_idx + 1, i, 1)
            total_ans = (total_ans + tree.sq_sum[1]) % MOD
            last_pos[val] = i

        return total_ans