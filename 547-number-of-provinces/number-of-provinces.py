class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adj=[[]for _ in range(n)]
        for u in range(n):
            for v in range(n):
                if isConnected[u][v]==1:
                    adj[u].append(v)
        parent=[i for i in range(n)]
        rank=[0]*n
        def find(x):
            if parent[x]==x:
                return x
            
            parent[x]=find(parent[x])
            
            return parent[x]

        def union(x,y):
            px=find(x)
            py=find(y)
            
            if px==py:
                return 
            if rank[px]>rank[py]:
                parent[py]=px
            elif rank[py]>rank[px]:
                parent[px]=py
            else:
                parent[px]=py
                rank[py]+=1

        for u in range(n):
            for v in adj[u]:
                pu=find(u)
                pv=find(v)

                if pu!=pv:
                    union(u,v)

        mp={}
        for i in range(n):
            leader=find(i)
            if leader in mp:
                mp[leader]+=1
            else:
                mp[leader]=1

        return len(mp)