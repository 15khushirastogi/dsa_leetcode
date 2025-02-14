class Solution {
private:
    int f(int i,vector<int>&nums,vector<int>&dp){
        if (i >= nums.size()) { 
            return 0;
        }
        if(dp[i]!=-1){
            return dp[i];
        }
        int rob=nums[i]+f(i+2,nums,dp);
        int notrob=f(i+1,nums,dp);

        dp[i]=max(rob,notrob);
        return dp[i];
    }
public:
    int rob(vector<int>& nums) {
        int n=nums.size();
        vector<int>dp(n,-1);
        return f(0,nums,dp);
    }
};