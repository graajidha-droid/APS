class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        max_diff = 0
        
        # Calculate initial differences
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        if not diffs:
            return 0
        
        max_diff = max(diffs)
        if max_diff == 0:
            return 0
            
        # Frequency array for differences
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1
            
        # Process from largest difference down to 1
        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue
                
            if k >= count[d]:
                k -= count[d]
                count[d - 1] += count[d]
                count[d] = 0
            else:
                count[d - 1] += k
                count[d] -= k
                k = 0
                break
                
        # Compute final sum of squared differences
        return sum(d * d * cnt for d, cnt in enumerate(count))