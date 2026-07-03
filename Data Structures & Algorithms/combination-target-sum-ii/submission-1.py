class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        def bt(ind,arr,cursum):
            if cursum==target:
                result.append(arr[:])                
                return

            if ind==len(nums) or cursum>target:
                return

            arr.append(nums[ind])
            bt(ind+1,arr,cursum+nums[ind])
            arr.pop()
            nextind=ind+1
            while nextind<len(nums) and nums[ind]==nums[nextind]:
                nextind+=1
            bt(nextind,arr,cursum)

        bt(0,[],0)
        return result      