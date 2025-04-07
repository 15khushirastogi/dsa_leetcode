class Solution {
private:
    int f(int i, vector<int>& dp, int n, vector<int>& cost){
        if(i==n-1){
            return cost[i];
        }
        if(i>=n){
            return 0;
        }
        if(dp[i]!=-1){
            return dp[i];
        }
        int onestep=f(i+1,dp,n,cost);
        int twostep=f(i+2,dp,n,cost);

        dp[i]=min(onestep,twostep)+cost[i];
        return dp[i];
    }
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n=cost.size();
        vector<int>dp(n,-1);
        return min(f(0,dp,n,cost),f(1,dp,n,cost));
    }
};