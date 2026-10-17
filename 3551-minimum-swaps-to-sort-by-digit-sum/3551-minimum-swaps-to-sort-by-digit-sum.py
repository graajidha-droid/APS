class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. calculate digit sum for a number
        def get_digit_sum(val):
            s = 0
            while val > 0:
                s += val % 10
                val //= 10
            return s
        
        # 2. store (digit_sum, value, original_index)
        arr = []
        for i, num in enumerate(nums):
            arr.append((get_digit_sum(num), num, i))
            
        # 3. sort based on digit_sum first, then value
        arr.sort()
        
        # 4. find minimum swaps using cycle decomposition
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # if element is already visited or already in correct position
            if visited[i] or arr[i][2] == i:
                continue
                
            cycle_size = 0
            curr = i
            
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][2]
                cycle_size += 1
                
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swaps