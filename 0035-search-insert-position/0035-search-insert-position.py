class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(right+left)//2
            if target==nums[mid]:
                return mid
            elif nums[mid]<target:
                left=mid+1
            #elif nums[mid]+1==target:
             #   return mid+1
            ##   return mid-1
            else:
                right=mid-1
        return left