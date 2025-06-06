class Solution {
private:
    int f(int i, int j, vector<vector<int>>& dp, vector<vector<int>>& grid){
        if(i==0 && j==0){
            return grid[i][j];
        }
        if(i<0 || j<0){
            return INT_MAX;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }

        int left=f(i,j-1,dp,grid);
        int up=f(i-1,j,dp,grid);

        dp[i][j]=grid[i][j]+min(left,up);

        return dp[i][j];
    }
public:
    int minPathSum(vector<vector<int>>& grid) {
        int ans=0;
        int m=grid.size();
        int n=grid[0].size();
        vector<vector<int>>dp(m,vector<int>(n,-1));

        return f(m-1,n-1,dp,grid);
    }
};