class Solution:
    def rob(self, cost: List[int]) -> int:
        n=len(cost)
        

        
        if n == 0: return 0
        if n == 1: return cost[0]
        if n == 2: return max(cost[0], cost[1])
        if n == 3: return max(cost[1], cost[0] + cost[2])


        mc=[0]*(n)
        mc[0]=cost[0]
        mc[1]=cost[1]
        mc[2]=cost[2]+cost[0]

        
        for i in range(3,len(cost)):
            mc[i]= cost[i] + max(mc[i-2],mc[i-3])
        
        return max(mc[-1],mc[-2])

