from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n   

        def bfs(start):
            q = deque([start])
            color[start] = 0  
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if color[nei] == color[node]: 
                        return False
                    if color[nei] == -1:        
                        color[nei] = 1 - color[node]
                        q.append(nei)
            return True

        for i in range(n):
            if color[i] == -1:
                if not bfs(i):
                    return False

        return True
