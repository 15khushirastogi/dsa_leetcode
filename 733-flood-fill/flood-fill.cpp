class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int m=image.size();
        int n=image[0].size();
        int originalColor = image[sr][sc];

        if (originalColor == color) return image;

        queue<pair<int,int>>q;
        q.push({sr,sc});
        image[sr][sc]=color;

        int drow[]={-1,0,+1,0};
        int dcol[]={0,+1,0,-1};

        while(!q.empty()){
            int row=q.front().first;
            int col=q.front().second;
            q.pop();

            for(int i=0;i<4;i++){
                int nrow=row+drow[i];
                int ncol=col+dcol[i];
                if(nrow>=0 && nrow<m && ncol>=0 && ncol<n && image[nrow][ncol]==originalColor){
                    q.push({nrow,ncol});
                    image[nrow][ncol]=color;
                }
            }
        }
        return image;
    }
};