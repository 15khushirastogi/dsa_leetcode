class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def f(n):
            if n==1:
                return 1
            if n==2:
                return 2
            if dp[n]!=-1:
                return dp[n]
            onestep=f(n-1)
            twostep=f(n-2)
            dp[n]=onestep+twostep
        
            return dp[n]

        return f(n)