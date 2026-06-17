class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1

        s=str(abs(x))
        s=s[::-1]
        x=int(s)
        if x in range(-2**31, 2**31):
            return x*sign
        return 0

        