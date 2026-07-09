class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        coun=Counter(nums)
        res=[]

        def bt(arr):
            if len(arr)==len(nums):
                res.append(arr[:])
                return
            
            for i in coun:
                if coun[i] > 0:                    
                    arr.append(i)
                    coun[i]-=1
                    bt(arr)
                    arr.pop()
                    coun[i]+=1                    

        
        bt([])
        return res
        