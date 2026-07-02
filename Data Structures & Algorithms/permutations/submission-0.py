class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def bt(arr):
            if len(arr)==len(nums):
                result.append(arr[:])
                return
            
            for num in nums:
                if num in arr:
                    continue
                arr.append(num)
                bt(arr)
                arr.pop()
            
        bt([])
        return result
