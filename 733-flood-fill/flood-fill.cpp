class Solution {
    void dfs(vector<vector<int>>& image, int row, int col, vector<vector<int>>&ans, int drow[], int dcol[], int newcolor, int originalcolor){
        ans[row][col]=newcolor;
        int m=image.size();
        int n=image[0].size();
        for(int i=0;i<4;i++){
            int nrow=row+drow[i];
            int ncol=col+dcol[i];
            if(nrow>=0 && nrow<m && ncol>=0 && ncol<n && image[nrow][ncol]==originalcolor && ans[nrow][ncol]!=newcolor){
                dfs(image, nrow, ncol, ans, drow, dcol, newcolor, originalcolor);
            }
        }
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newcolor) {
        int originalcolor=image[sr][sc];
        vector<vector<int>>ans=image;
        int drow[]={-1,0,1,0};
        int dcol[]={0,+1,0,-1};
        dfs(image,sr,sc,ans,drow,dcol,newcolor,originalcolor);

        return ans;
    }
};