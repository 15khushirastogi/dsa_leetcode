class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(n+1)
        def f(ind):
            if ind==n-1:
                return cost[ind]
            if ind==n-2:
                return cost[ind]
            if dp[ind]!=-1:
                return dp[ind]
            onestep=cost[ind]+f(ind+1)
            twostep=cost[ind]+f(ind+2)
            dp[ind]=min(onestep,twostep)

            return dp[ind]
        return min(f(0),f(1))