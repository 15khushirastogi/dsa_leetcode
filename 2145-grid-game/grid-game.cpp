class Solution {
public:
    long long gridGame(vector<vector<int>>& grid) {
        long long topsum=0;
        int n=grid[0].size();
        for(int i=0;i<n;i++){
            topsum+=grid[0][i];
        }
        long long bottomsum=0;
        long long ans=LLONG_MAX;
        for(int p=0;p<n;p++){
            topsum-=grid[0][p];
            ans=min(ans,max(topsum,bottomsum));
            bottomsum+=grid[1][p];
        }
        return ans;
    }
};