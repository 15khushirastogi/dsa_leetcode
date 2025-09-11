class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj=[[]for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis=[0]*n
        size=[]
        comp=0
        def dfs(node):
            vis[node]=1
            count=1
            for nei in adj[node]:
                if not vis[nei]:
                    count+=dfs(nei)
            return count
        for i in range(n):
            if vis[i]==0:
                size.append(dfs(i))

        rem=n
        result=0
        for s in size:
            result+=s*(rem-s)
            rem-=s

        return result