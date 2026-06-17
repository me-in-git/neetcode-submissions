class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        l=0
        for r in range(1,len(prices)):
            maxi=max(prices[r]-prices[l],maxi)
            if prices[l]>prices[r]:
                l=r
            
        return maxi


        