class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        cnt=0
        vis=[[0 for _ in range(n)] for _ in range(m)]
        def dfs(i,j):
            vis[i][j]=1
            dir=[[0,1],[1,0],[0,-1],[-1,0]]
            for dr in dir:
                newr=i+dr[0]
                newc=j+dr[1]
                if newr>=0 and newc>=0 and newr<m and newc<n and grid[newr][newc]=='1' and vis[newr][newc]==0:
                    dfs(newr,newc)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and vis[i][j]==0:
                    cnt+=1
                    dfs(i,j)

        return cnt