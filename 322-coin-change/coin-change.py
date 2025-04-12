class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[0 for _ in range(amount+1)] for _ in range(n)]
        #when we reach the first element
        for i in range(amount+1):
            if(i%coins[0]==0):
                dp[0][i]=i//coins[0]
            else:
                dp[0][i]=float('inf')
        for ind in range(1,n):
            for target in range(amount+1):
                nottake=0+dp[ind-1][target]
                take=float('inf')
                if(target>=coins[ind]):
                    take=1+dp[ind][target-coins[ind]]
                
                dp[ind][target]=min(take,nottake)


        res=dp[n-1][amount]
        if(res!=float('inf')):
            return res
        else:
            return -1