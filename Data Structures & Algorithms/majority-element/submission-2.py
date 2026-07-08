class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k=nums[0]
        v=1
        for i in range(1,len(nums)):

            if nums[i]==k:
                v+=1
            else:
                v-=1

            if v==0:
                k=nums[i]
                v=1
        
        return k
            

        