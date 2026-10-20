class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        def is_sortable(k: int) -> bool:
            for i in range(0, n, k):
                # 1. Check if multiset of elements matches the target sorted block
                block = nums[i : i + k]
                target_block = sorted_nums[i : i + k]
                
                if sorted(block) != target_block:
                    return False
                
                # 2. Count cyclic drops in the block
                drops = 0
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        drops += 1
                        if drops > 1:
                            return False
                            
            return True

        total_sum = 0
        
        # Iterate over all possible divisors of n
        for k in range(1, n + 1):
            if n % k == 0:
                if is_sortable(k):
                    total_sum += k
                    
        return total_sum