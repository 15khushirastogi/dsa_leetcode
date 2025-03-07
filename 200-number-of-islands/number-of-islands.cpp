class Solution {
private:
    void bfs(int r, int c, vector<vector<int>>&visited, int m, int n, vector<vector<char>>& grid){
        queue<pair<int,int>>q;
        q.push({r,c});
        visited[r][c]=1;
        int dr[]={-1,0,+1,0};
        int dc[]={0,+1,0,-1};
        while(!q.empty()){
            int row=q.front().first;
            int col=q.front().second;
            q.pop();
            for(int i=0;i<4;i++){
                int newr=row+dr[i];
                int newc=col+dc[i];

                if(newr>=0 && newr<m && newc>=0 && newc<n && visited[newr][newc]!=1 && grid[newr][newc]=='1'){
                    q.push({newr,newc});
                    grid[newr][newc]='0';
                }
            }
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        int island=0;
        int m=grid.size();
        int n=grid[0].size();
        vector<vector<int>>visited(m,vector<int>(n,0));
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]=='1'){
                    island+=1;
                    bfs(i,j,visited,m,n,grid);
                }
            }
        }
        return island;
    }
};