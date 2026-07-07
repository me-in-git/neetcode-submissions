class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a &= mask
        b &= mask
        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        # now a is in [0, 0xFFFFFFFF]
        if a & 0x80000000:
            return ~(a ^ mask)  # or a - 0x100000000
        return a
