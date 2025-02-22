class Solution1 {
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

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int row = grid.size();
        int col = grid[0].size();
        int perimeter = 0;
        
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    if (i == 0 || grid[i - 1][j] == 0) perimeter++; 
                    if (j == 0 || grid[i][j - 1] == 0) perimeter++; 
                    if (i == row - 1 || grid[i + 1][j] == 0) perimeter++; 
                    if (j == col - 1 || grid[i][j + 1] == 0) perimeter++; 
                }
            }
        }
        return perimeter;
    }
};
