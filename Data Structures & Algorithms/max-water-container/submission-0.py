class Solution:
    def maxArea(self, heights: List[int]) -> int:
        tot=0
        maxi=0
        r=len(heights)-1
        l=0
        while r>l:
            tot=(r-l)*min(heights[r],heights[l])
            maxi=max(maxi,tot)
            if heights[r]<heights[l]:
                r-=1
            else:
                l+=1
        return maxi


        