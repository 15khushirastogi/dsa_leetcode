class Solution {
private:
    bool f(int idx, int target, vector<vector<int>> &dp, vector<int> &nums){
        if(target==0){
            return true;
        }
        if(idx==0){
            return target==nums[idx];
        }
        if(dp[idx][target]!=-1){
            return dp[idx][target];
        }

        bool notTake=f(idx-1,target,dp,nums);
        bool take=false;
        if(target>=nums[idx]){
            take=f(idx-1,target-nums[idx],dp,nums);
        }

        return dp[idx][target]=take || notTake;
    }
public:
    bool canPartition(vector<int>& nums) {
        int n=nums.size();
        int target=0;
        for(int i=0;i<n;i++){
            target+=nums[i];
        }
        if(target%2!=0){
            return false;
        }
        target=target/2;
        vector<vector<int>>dp(n+1,vector<int>(target+1,-1));
        return f(n-1,target,dp,nums);
    }
};