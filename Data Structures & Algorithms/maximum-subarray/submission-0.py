class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs=float("-inf")
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            maxs=max(maxs,s)
            if s<0:
                s=0
        return maxs



        