class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def bt(arr):
            if len(arr)==len(nums):
                res.append(arr[:])
                return
            
            for i in nums:
                if i in arr:
                    continue
                else:
                    arr.append(i)
                    bt(arr)
                    arr.pop()
            
        bt([])
        return res