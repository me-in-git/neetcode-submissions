class Solution:
    def isHappy(self, n: int) -> bool:
        sett=set()

        def ss(n):
            s=0
            while n>0:
                s+=(n%10)**2
                n=n//10
            return s

        while n>0:
            if n==1:
                return True
            if n in sett:
                return False            
            sett.add(n)
            n=ss(n)
            

        return n==1

        