class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def dfs(i,j):
            grid[i][j]=0
            dir=[[0,1],[1,0],[0,-1],[-1,0]]

            for dr in dir:
                newr=i+dr[0]
                newc=j+dr[1]

                if newr>=0 and newr<m and newc>=0 and newc<n and grid[newr][newc]==1:
                    dfs(newr,newc)

        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    if grid[i][j]==1:
                        dfs(i,j)
                    

        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    cnt+=1
        return cnt