class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        island=0
        visited=[[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    island+=1
                    def bfs(r,c):
                        q=deque()
                        q.append([r,c])
                        visited[r][c]=1
                        dr=[-1,0,+1,0]
                        dc=[0,+1,0,-1]
                        while q:
                            row,col=q.popleft()
                            for i in range(4):
                                newr=row+dr[i]
                                newc=col+dc[i]

                                if newr>=0 and newr<m and newc>=0 and newc<n and visited[newr][newc]!=1 and grid[newr][newc]=='1':
                                    q.append([newr,newc])
                                    grid[newr][newc]='0'
                    bfs(i,j)

        return island