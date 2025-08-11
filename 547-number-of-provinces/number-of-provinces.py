class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row=len(isConnected)
        col=len(isConnected[0])
        cnt=0
        vis=[0 for _ in range(row)]
        
        def dfs(i):
            vis[i]=1
            for j in range(col):
                if isConnected[i][j]==1 and vis[j]==0:
                    dfs(j)
        for i in range(row):
            if vis[i]==0:
                cnt+=1
                dfs(i)

        return cnt
