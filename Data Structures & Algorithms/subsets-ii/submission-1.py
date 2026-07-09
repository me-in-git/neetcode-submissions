class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        def bt(arr,ind):
            if ind==len(nums):
                res.append(arr[:])
                return
            
            arr.append(nums[ind])
            bt(arr,ind+1)
            arr.pop()
            while ind+1<len(nums) and nums[ind]==nums[ind+1]:
                ind+=1
            bt(arr,ind+1)
        
        bt([],0)
        return res