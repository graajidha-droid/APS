class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s=min(nums)
        l=max(nums)
        #if len(nums)==1:
         #   if nums[0]==0:
          #      return 1
           # else:
            #    return 0
        for i in range (l+2):
            if i not in nums:
                return i