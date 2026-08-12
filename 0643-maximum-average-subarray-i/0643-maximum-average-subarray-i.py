class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=0
        for i in range (k):
            window_sum+=nums[i]
        max_sum=window_sum
        for i in range(k,len(nums)):
            window_sum=window_sum-nums[i-k]+nums[i]
            if max_sum<window_sum:
                max_sum=window_sum
        max_avg=max_sum/k
        return max_avg