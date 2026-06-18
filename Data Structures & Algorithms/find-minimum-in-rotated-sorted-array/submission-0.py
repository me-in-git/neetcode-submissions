class Solution:
    def findMin(self, nums: List[int]) -> int:

        l=0
        r=len(nums)-1
        while r>l:
            mid=(r+l)//2
            if nums[mid]<nums[-1]:
                r=mid
            else:
                l=mid+1
            if nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]:
                return nums[mid]
        return nums[l]
        
        
        