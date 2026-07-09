class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]

        def bt(ind, arr, summ):
            if summ==target:
                res.append(arr[:])
                return
            
            if summ>target or len(nums)==ind:
                return
            

            arr.append(nums[ind])            
            bt(ind+1,arr,summ+nums[ind])
            arr.pop()

            nind=ind+1
            while nind < len(nums) and nums[ind]==nums[nind]:
                nind+=1
            bt(nind,arr,summ)        
        bt(0,[],0)
        
        return res