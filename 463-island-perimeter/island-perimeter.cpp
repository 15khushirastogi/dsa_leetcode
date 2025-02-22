class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int row=grid.size();
        int col=grid[0].size();
        queue<pair<int,int>>q;
        int perimeter=0;
        int dirx[]={-1,0,+1,0};
        int diry[]={0,+1,0,-1};

        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(grid[i][j]==1){
                    q.push({i,j});
                }
            }
        }
        while(!q.empty()){
            int r=q.front().first;
            int c=q.front().second;
            q.pop();
            
            for(int i=0;i<4;i++){
                int newr=r+dirx[i];
                int newc=c+diry[i];

                if(newr<0 || newc<0 || newr==row || newc==col){
                    perimeter++;
                }
                if(newr>=0 && newr<row && newc>=0 && newc<col && grid[newr][newc]==0){
                    perimeter++;
                }
            }
        }
        return perimeter;
    }
};