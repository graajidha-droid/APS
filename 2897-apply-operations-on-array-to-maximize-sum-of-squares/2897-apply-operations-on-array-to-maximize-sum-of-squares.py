class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # count set bits at each position up to bit 30
        bit_count = [0] * 31
        for num in nums:
            for i in range(31):
                if (num >> i) & 1:
                    bit_count[i] += 1
                    
        total_sum = 0
        
        # greedily construct the k largest numbers
        for _ in range(k):
            val = 0
            for i in range(31):
                if bit_count[i] > 0:
                    val |= (1 << i)
                    bit_count[i] -= 1
            total_sum = (total_sum + val * val) % MOD
            
        return total_sum