class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h=defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in h:
                for ind in h[nums[i]]:
                    if abs(ind-i)<=k:
                        return True
            
            h[nums[i]].append(i)
        
        return False
        