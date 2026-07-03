class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        def bt(arr,ind):
            if len(nums)==ind:
                result.append(arr[:])
                return

            arr.append(nums[ind])
            bt(arr,ind+1)
            arr.pop()
            nextind=ind+1
            while nextind<len(nums) and nums[ind]==nums[nextind]:
                nextind+=1
            bt(arr,nextind)
        
        bt([],0)
        return result
        