class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # result=[]
        # def bt(ind,arr,cursum):
        #     if sum(arr)==target:
        #         result.append(arr[:])
        #         return
        #     if ind==len(nums) or cursum>target:
        #         return

        #     arr.append(nums[ind])
        #     bt(ind,arr,cursum+nums[ind])
        #     arr.pop()
        #     bt(ind+1,arr,cursum)


        # bt(0,[],0)
        # return result

        res=[]

        def bt(arr,summ,ind):
            
            if summ == target :
                res.append(arr[:])
                return
            
            if summ > target or len(nums)==ind:
                return
            
            arr.append(nums[ind])
            bt(arr,summ+nums[ind],ind)
            arr.pop()
            bt(arr,summ,ind+1)
        
        bt([],0,0)
        
        return res