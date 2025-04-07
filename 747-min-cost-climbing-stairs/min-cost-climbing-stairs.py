class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*n
        def f(idx):
            if(idx==n-1):
                return cost[idx]
            if(idx>=n):
                return 0
            if(dp[idx]!=-1):
                return dp[idx]
            onestep=f(idx+1)
            twostep=f(idx+2)

            dp[idx]=min(onestep,twostep)+cost[idx]

            return dp[idx]
        return min(f(0),f(1))
