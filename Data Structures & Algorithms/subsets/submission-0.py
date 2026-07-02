class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def backtra(ind,arr):
            if ind==len(nums):
                result.append(arr[:])
                return
            
           
            arr.append(nums[ind])
            backtra(ind+1,arr)
            arr.pop()
            backtra(ind+1,arr)


        backtra(0,[])
        return result