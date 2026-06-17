class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        fin=0
        for i in range(1,len(nums)+1):
            fin^=i
        for n in nums:
            fin^=n
        return fin


        