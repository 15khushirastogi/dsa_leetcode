class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        rank=[0]*n
        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent_x=find(x)
            parent_y=find(y)
            if parent_x==parent_y:
                return 
            if rank[parent_x]>rank[parent_y]:
                parent[parent_y]=parent_x
            elif rank[parent_y]>rank[parent_x]:
                parent[parent_x]=parent_y
            else:
                parent[parent_x]=parent_y
                rank[parent_y]+=1
            
        for edg in edges:
            u=edg[0]
            v=edg[1]
            parent_u=find(u)
            parent_v=find(v)
            if parent_u!=parent_v:
                union(u,v)

        mp={}
        for i in range(n):
            leader=find(i)
            if leader in mp:
                mp[leader]+=1
            else:
                mp[leader]=1

        result=0
        rem=n
        for comp,size in mp.items():
            result+=size*(rem-size)
            rem=rem-size
        
        return result