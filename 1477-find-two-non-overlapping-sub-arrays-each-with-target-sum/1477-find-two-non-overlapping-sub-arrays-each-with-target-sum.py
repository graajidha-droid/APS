class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        best = [float('inf')] * (n + 1)
        prefix = {0: 0}

        total = 0
        answer = float('inf')

        for i in range(1, n + 1):
            total += arr[i - 1]

            best[i] = best[i - 1]

            if total - target in prefix:
                j = prefix[total - target]

                length = i - j

                # Best subarray completely before this one
                if best[j] != float('inf'):
                    answer = min(answer, best[j] + length)

                best[i] = min(best[i], length)

            prefix[total] = i

        return -1 if answer == float('inf') else answer