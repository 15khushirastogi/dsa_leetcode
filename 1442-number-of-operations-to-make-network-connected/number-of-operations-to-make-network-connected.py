class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        
        graph=[[] for _ in range(n)]
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)

        vis=[0]*n
        def dfs(i):
            vis[i]=1
            for nei in graph[i]:
                if not vis[nei]:
                    dfs(nei)

        components=0
        for i in range(n):
            if vis[i]==0:
                dfs(i)
                components+=1

        return components-1