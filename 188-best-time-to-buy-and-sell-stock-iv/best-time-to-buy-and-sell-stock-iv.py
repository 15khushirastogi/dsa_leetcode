class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0 for _ in range(k+1)]for _ in range(2)]for _ in range(n+1)]

        #Base Cases
        for ind in range(0,n):
            for buy in range(2):
                dp[ind][buy][0]=0

        for buy in range(2):
            for cap in range(k+1):
                dp[n][buy][cap]=0

        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,k+1):
                    if buy:
                        take=-prices[ind]+dp[ind+1][0][cap]
                        nottake=0+dp[ind+1][1][cap]

                        dp[ind][buy][cap]=max(take,nottake)
                    else:
                        sell=prices[ind]+dp[ind+1][1][cap-1]
                        notsell=0+dp[ind+1][0][cap]

                        dp[ind][buy][cap]=max(sell,notsell)

        return dp[0][1][k]