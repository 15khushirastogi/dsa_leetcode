class Solution {
private:
    int f(int i, int j, vector<vector<int>>& dp,vector<vector<int>>& triangle, int n){
        if(i==n-1){
            return triangle[i][j];
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        int bottom=f(i+1,j,dp,triangle,n);
        int diagonal=f(i+1,j+1,dp,triangle,n);

        dp[i][j]=min(bottom, diagonal)+triangle[i][j];

        return dp[i][j];
    }
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n=triangle.size();
        vector<vector<int>>dp(n,vector<int>(n,-1));
        return f(0,0,dp,triangle,n);
    }
};