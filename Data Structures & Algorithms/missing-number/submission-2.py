class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter=0
        nums.sort()
        for n in nums:
            if n==counter:
                pass
            else:
                return counter
            counter+=1
        return counter


        