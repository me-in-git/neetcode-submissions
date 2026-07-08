class Solution:
    def search(self, nums: List[int], target: int) -> int:

        mini=0
        maxi=len(nums)-1

        while mini<= maxi:
            mid=(mini+maxi)//2

            if target==nums[mid]:
                return mid
                
            if nums[mid]>= nums[mini]:
                if nums[mini]<=target<=nums[mid]:
                    maxi=mid-1
                else:
                    mini=mid+1
            else:
                if nums[maxi]>= target >= nums[mid]:
                    mini=mid+1
                else:
                    maxi=mid-1
        
        return -1


        