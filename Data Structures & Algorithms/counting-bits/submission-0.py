class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            tot=0
            while n>0:
                if n%2!=0:
                    tot+=1
                n=n//2
            return tot
        res=[count(i) for i in range(n+1)]
        return res
        