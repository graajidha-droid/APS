class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mi=prices[0]
        ma=0
        for i in range(1,len(prices)):
            if prices[i]<mi:
                mi=prices[i]
            else:
                if prices[i]-mi >ma:
                    ma=prices[i]-mi
        return ma