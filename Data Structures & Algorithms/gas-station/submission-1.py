class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        new=[gas[i]-cost[i] for i in range(len(gas))]


        summ=0
        start=0
        curr=0
        for i in range(len(new)):
            summ+=new[i]
            curr+=new[i]

            if curr<0:
                start=i+1
                curr=0
            
        return start if summ>=0 else -1

        
