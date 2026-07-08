class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        c1=0
        c2=0
        c3=0
        for trip in triplets:
            a,b,c = trip[0],trip[1],trip[2]
            if a>target[0] or b>target[1] or c>target[2]:
                pass
            else:
                if a==target[0]:
                    c1=1
                if b==target[1]:
                    c2=1
                if c==target[2]:
                    c3=1
        
        if c1 and c2 and c3:
            return True
        return False
                