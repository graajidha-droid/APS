class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        k = len(nums)
        result = 0
        
        for i in range(k):
            # Check if total length k is divisible by 1-based index (i + 1)
            if k % (i + 1) == 0:
                result += nums[i] ** 2
                
        return result