class Solution {
private:
    int ways(int n, vector<int>& dp){
        // define base cases
        if(n==0){
            return 1;
        }
        if(n<0){
            return 0;
        }
        //check dp for the already solved subproblems
        if(dp[n]!=-1){
            return dp[n];
        }
        //store the result in dp
        dp[n]=ways(n-1,dp)+ways(n-2,dp);
        return dp[n];
    }
public:
    int climbStairs(int n) {
        //declare and initialise dp
        vector<int>dp(n+1,-1);
        return ways(n,dp);
    }
};