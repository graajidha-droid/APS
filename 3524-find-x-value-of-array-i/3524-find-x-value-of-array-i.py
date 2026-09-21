class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            r = num % k

            # Start a new subarray
            new_dp[r] += 1

            # Extend previous subarrays
            for old in range(k):
                new = (old * r) % k
                new_dp[new] += dp[old]

            # Add to final answer
            for i in range(k):
                ans[i] += new_dp[i]

            dp = new_dp

        return ans