class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        
        mc=[0]*(n)
        mc[0]=cost[0]
        mc[1]=cost[1]

        for i in range(2,len(cost)):
            mc[i]= cost[i] + min(mc[i-1],mc[i-2])
        
        return min(mc[-1],mc[-2])


