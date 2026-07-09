class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        
        def bt(arr,ind):
            if len(arr)==k:
                res.append(arr[:])                
                return 
            if ind==n:
                return             
            
            arr.append(ind+1)
            bt(arr,ind+1)
            arr.pop()
            bt(arr,ind+1)

        bt([],0)
        return res