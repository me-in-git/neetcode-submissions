class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float("inf")
        
        l=0
        summ=0

        for r in range(len(nums)):
            summ+=nums[r]
            while summ>=target and l<len(nums):
                mini=min(mini,(r-l+1))                
                summ-=nums[l]
                l+=1
            
        return 0 if mini==float("inf") else mini

        