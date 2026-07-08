class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini=1
        maxi=max(piles)

        def check(piles,kval):
            hrs=0
            for num in piles:
                hrs+=(num+k-1)//kval
                if hrs>h:
                    return False
            if hrs<=h:
                return True
            return False
        
        while mini< maxi:
            k=(mini+maxi)//2
            if check(piles,k):
                maxi=k
            else:
                mini=k+1
            
        return maxi
