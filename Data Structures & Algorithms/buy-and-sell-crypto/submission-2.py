class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        l=0
        maxp=0
        for r in range(1,len(prices)):
            if prices[r]>prices[l]:
                maxp=max(maxp,prices[r]-prices[l])
            else:
                l=r
                
        return maxp

