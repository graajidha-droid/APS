class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        left_best = [[0] * n for _ in range(n)]
        right_best = [[0] * n for _ in range(n)]

        for i in range(n):
            left_best[i][i] = right_best[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            k = 0

            for l in range(n - length + 1):
                r = l + length - 1

                if k < l:
                    k = l

                while k < r:
                    left_sum = prefix[k + 1] - prefix[l]
                    right_sum = prefix[r + 1] - prefix[k + 1]

                    if left_sum < right_sum:
                        k += 1
                    else:
                        break

                best = 0

                if k > l:
                    best = max(best, left_best[l][k - 1])

                if k <= r:
                    left_sum = prefix[k + 1] - prefix[l]
                    right_sum = prefix[r + 1] - prefix[k + 1]

                    if k < r and left_sum == right_sum:
                        best = max(
                            best,
                            left_best[l][k],
                            right_best[k + 1][r]
                        )
                    elif k < r:
                        best = max(best, right_best[k + 1][r])

                dp[l][r] = best

                total = prefix[r + 1] - prefix[l]

                left_best[l][r] = max(
                    left_best[l][r - 1],
                    total + dp[l][r]
                )

                right_best[l][r] = max(
                    right_best[l + 1][r],
                    total + dp[l][r]
                )

        return dp[0][n - 1]