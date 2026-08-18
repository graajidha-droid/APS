class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = {}

        for i in range(n - k + 1):
            seen = set(nums[i:i + k])

            for num in seen:
                count[num] = count.get(num, 0) + 1

        ans = -1

        for num in count:
            if count[num] == 1:
                ans = max(ans, num)

        return ans