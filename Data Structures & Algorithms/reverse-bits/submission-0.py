class Solution:
    def reverseBits(self, n: int) -> int:
        s=""
        while n>0:
            s+=str(n%2)
            n=n//2
        while len(s) < 32:
            s += "0"

        res=0
        powa=1
        for ch in s[::-1]:
            res+=int(ch)*powa
            powa*=2
        return res

        
        