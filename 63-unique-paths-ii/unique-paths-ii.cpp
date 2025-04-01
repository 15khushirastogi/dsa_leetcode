class Solution1 {
private:
    int f(int i, int j, vector<vector<int>>& dp, vector<vector<int>>& obstacleGrid){
        //base conditions
        if(i==0 && j==0){
            return 1;
        }
        if(i<0 || j<0){
            return 0;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        //recursive conditions
        if(obstacleGrid[i][j]==1){
            dp[i][j]=0;
            return 0;
        }
        else{
            int up=f(i-1,j,dp,obstacleGrid);
            int left=f(i,j-1,dp,obstacleGrid);

            dp[i][j]=up+left;

        }
        return dp[i][j];

    }
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int count=0;
        int m=obstacleGrid.size();
        int n=obstacleGrid[0].size();
        if(obstacleGrid[0][0]==1 || obstacleGrid[m-1][n-1]==1){
            return 0;
        }
        vector<vector<int>>dp(m,vector<int>(n,-1));
        return f(m-1,n-1,dp,obstacleGrid);
    }
};

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int count=0;
        int m=obstacleGrid.size();
        int n=obstacleGrid[0].size();
        if(obstacleGrid[0][0]==1 || obstacleGrid[m-1][n-1]==1){
            return 0;
        }
        vector<vector<int>>dp(m,vector<int>(n,0));
        dp[0][0]=1;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                int up=0;
                int left=0;
                if(obstacleGrid[i][j]==1){
                    dp[i][j]=0;
                }
                else{
                    if (i > 0) dp[i][j] += dp[i-1][j];
                    if (j > 0) dp[i][j] += dp[i][j-1];
                }
            }
        }
        return dp[m-1][n-1];
    }
};