class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def bt(arr,ind):
            if len(nums)==ind:
                res.append(arr[:])
                return
            
            arr.append(nums[ind])
            bt(arr,ind+1)
            arr.pop()
            bt(arr,ind+1)
        
        bt([],0)
        return res
