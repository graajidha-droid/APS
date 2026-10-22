class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        idx0 = nums.index(0)
        
        # Check if cyclically increasing
        is_inc = True
        for i in range(n):
            if nums[(idx0 + i) % n] != i:
                is_inc = False
                break
                
        if is_inc:
            # Option A: Left rotations only
            # Option B: Reverse -> Rotate -> Reverse
            return min(idx0, n - idx0 + 2)
            
        # Check if cyclically decreasing
        is_dec = True
        for i in range(n):
            if nums[(idx0 - i + n) % n] != i:
                is_dec = False
                break
                
        if is_dec:
            # Option A: Reverse -> Rotate
            # Option B: Rotate -> Reverse
            return min(n - idx0, idx0 + 2)
            
        return -1