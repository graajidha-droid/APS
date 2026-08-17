class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pot=[]
        co=0
        for num in nums:
            co+=num
            pot.append(co)
        return pot