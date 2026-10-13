class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted([x * x for x in nums])
        n = len(nums)
        
        # number of negative terms
        k = n // 2
        
        # subtract the smallest k squared values, add the rest
        return sum(squares[k:]) - sum(squares[:k])