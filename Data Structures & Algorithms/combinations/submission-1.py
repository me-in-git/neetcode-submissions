class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[i for i in range(1,n+1)]
        print(nums)
        res=[]
        
        def bt(arr,ind):
            if  len(arr)==k:
                res.append(arr[:])                
                return 
            if ind==len(nums):
                return 
            
            
            arr.append(nums[ind])
            bt(arr,ind+1)
            arr.pop()
            bt(arr,ind+1)

        bt([],0)
        return res