class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj=[[]for _ in range(n)]
        for u,v in paths:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)

        color=[0]*n
        for i in range(n):
            used=set(color[nei] for nei in adj[i])
            for j in range(1,5):
                if j not in used:
                    color[i]=j


        return color
        