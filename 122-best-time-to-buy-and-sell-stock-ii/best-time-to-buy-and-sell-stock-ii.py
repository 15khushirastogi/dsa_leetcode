class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1 for _ in range(2)]for _ in range(n+1)]

        def f(ind,buy):
            if ind==n:
                return 0
            
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy:
                take=-prices[ind]+f(ind+1,0)
                nottake=0+f(ind+1,1)
                profit=max(take,nottake)

            else:
                sell=prices[ind]+f(ind,1)
                notsell=0+f(ind+1,0)
                profit=max(sell,notsell)

            dp[ind][buy]=profit
            return profit

        return f(0,1)

        