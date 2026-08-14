class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum=0
        left=0
        min_size=float('inf')
        for right in range (len(nums)):
            window_sum+=nums[right]
            while window_sum>=target:
                current_length=right-left+1
                if current_length<min_size:
                    min_size=current_length
                window_sum-=nums[left]
                left+=1

        if min_size==float('inf'):
            return 0
        else:
            return min_size