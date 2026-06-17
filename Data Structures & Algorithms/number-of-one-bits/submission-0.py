class Solution:
    def hammingWeight(self, n: int) -> int:
        tot=0
        while n>0:
            if n%2!=0:
                tot+=1
            n=n//2
        return tot
        