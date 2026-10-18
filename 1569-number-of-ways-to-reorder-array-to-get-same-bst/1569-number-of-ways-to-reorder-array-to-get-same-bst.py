import math
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # number of ways to interleave left and right arrays
            ways = math.comb(len(left) + len(right), len(left)) % MOD
            
            return (ways * dfs(left) % MOD * dfs(right) % MOD)
        
        # subtract 1 because the original array ordering is excluded
        return (dfs(nums) - 1) % MOD