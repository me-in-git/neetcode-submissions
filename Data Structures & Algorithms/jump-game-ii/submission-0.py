class Solution:
    def jump(self, nums: List[int]) -> int:

        l=0
        r=0
        jumps=0
        maxin=0
        while r<len(nums)-1:
            jumps+=1
            for i in range(l,r+1):
                maxin=max(maxin,i+nums[i])
            l=r+1
            r=maxin
        
        return jumps





            
        