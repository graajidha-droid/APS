class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        prefix_sum=0
        count=0
        
        for num in nums:
            prefix_sum+=num
            needed=prefix_sum-k
            if needed in freq:
                count+=freq[needed]
            if prefix_sum in freq:
                freq[prefix_sum]+=1
            else:
                freq[prefix_sum]=1
        return count