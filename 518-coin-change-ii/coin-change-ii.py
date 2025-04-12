class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[-1 for _ in range(amount+1)] for _ in range(n)]
        def f(ind,target):
            if(ind==0):
                if(target%coins[0]==0):
                    return 1
                else:
                    return 0

            if(dp[ind][target]!=-1):
                return dp[ind][target]

            nottake=f(ind-1,target)
            take=0
            if(target>=coins[ind]):
                take=f(ind,target-coins[ind])

            dp[ind][target]=take+nottake
            return dp[ind][target]

        res=f(n-1,amount)
        if(res==-1):
            return 0
        else:
            return res
