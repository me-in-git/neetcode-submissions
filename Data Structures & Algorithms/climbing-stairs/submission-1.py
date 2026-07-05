from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1:
            return 1

        arr=[0]*(n+1)
        arr[1]=1
        arr[2]=2

        @lru_cache
        def dp(n):
            if n==2:
                return 2
            if n==1:
                return 1
            if n<=0:
                return 0
            return dp(n-1)+dp(n-2)
        
        return dp(n)
