from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1 for _ in range(amount+1)] for _ in range(n)]
        def f(ind,target):
            if(ind==0):
                if(target%coins[ind]==0):
                    return target//coins[0]
                else:
                    return float('inf')

            if(dp[ind][target]!=-1):
                return dp[ind][target]
            nottake=0+f(ind-1,target)
            take=float('inf')
            if(target>=coins[ind]):
                take=1+f(ind,target-coins[ind])
            
            dp[ind][target]=min(take,nottake)

            return dp[ind][target]

        res=f(n-1,amount)
        if(res!=float('inf')):
            return res
        else:
            return -1

