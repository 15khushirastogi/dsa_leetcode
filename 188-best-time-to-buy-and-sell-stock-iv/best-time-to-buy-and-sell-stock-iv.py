class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1 for _ in range(k+1)]for _ in range(2)]for _ in range(n+1)]

        def f(ind,buy,cap):
            if ind==n:
                return 0
            if cap==0:
                return 0
            if dp[ind][buy][cap]!=-1:
                return dp[ind][buy][cap]
            if buy:
                take=-prices[ind]+f(ind+1,0,cap)
                nottake=0+f(ind+1,1,cap)

                dp[ind][buy][cap]=max(take,nottake)
            else:
                sell=prices[ind]+f(ind+1,1,cap-1)
                notsell=0+f(ind+1,0,cap)

                dp[ind][buy][cap]=max(sell,notsell)

            return dp[ind][buy][cap]

        return f(0,1,k)