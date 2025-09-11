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

        total_pairs = n * (n - 1) // 2

        for s in size:
            total_pairs -= s * (s - 1) // 2

        return total_pairs