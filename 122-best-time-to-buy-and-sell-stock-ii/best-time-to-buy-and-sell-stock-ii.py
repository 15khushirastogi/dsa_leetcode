class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1 for _ in range(2)]for _ in range(n+1)]

        dp[n][0]=dp[n][1]=0
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    take=-prices[ind]+dp[ind+1][0]
                    nottake=0+dp[ind+1][1]
                    dp[ind][buy]=max(take,nottake)

                else:
                    sell=prices[ind]+dp[ind+1][1]
                    notsell=0+dp[ind+1][0]
                    dp[ind][buy]=max(sell,notsell)

        return dp[0][1]

        