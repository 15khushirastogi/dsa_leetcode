class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adj=[[]for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    adj[i].append(j)
        count=0
        def dfs(node):
            vis[node]=1
            for nei in adj[node]:
                if vis[nei]==0:
                    dfs(nei)
        
        vis=[0]*n
        for i in range(n):
            if vis[i]==0:
                count+=1
                dfs(i)

        return count