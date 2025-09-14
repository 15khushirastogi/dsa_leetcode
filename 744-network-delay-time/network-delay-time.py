import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        
        pq=[]
        heapq.heappush(pq,[0,k])
        min_time=[float('inf')]*(n+1)
        min_time[k]=0
        while pq:
            time,node=heapq.heappop(pq)
            for next_node,next_time in adj[node]:
                if time+next_time<min_time[next_node]:
                    min_time[next_node]=time+next_time
                    heapq.heappush(pq,[time+next_time,next_node])
        max_time = max(min_time[1:])
        
        return max_time if max_time != float('inf') else -1