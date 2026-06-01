class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        print(nums)

        leng=1
        maxi=1
        for i in range(1,len(nums)):            
            if nums[i]-nums[i-1]==1:
                leng+=1
            elif nums[i]-nums[i-1]>1:
                maxi=max(maxi,leng)
                leng=1
            maxi=max(maxi,leng)

        return maxi


            