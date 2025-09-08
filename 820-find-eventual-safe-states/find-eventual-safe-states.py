from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0] * n   

        def dfs(node: int) -> bool:
            if vis[node] != 0:
                return vis[node] == 2  

            vis[node] = 1
            for nei in graph[node]:
                if vis[nei] == 1 or not dfs(nei):
                    return False
            vis[node] = 2 
            return True

        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans
