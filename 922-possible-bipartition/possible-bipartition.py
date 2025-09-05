class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjlist=[[]for _ in range(n+1)]
        for u,v in dislikes:
            adjlist[u].append(v)
            adjlist[v].append(u)

        color=[-1]*(n+1)
        def dfs(cur,curcolor):
            color[cur]=curcolor
            for nei in adjlist[cur]:
                if color[nei]==curcolor:
                    return False
                if color[nei]==-1:
                    neicolor=1-curcolor
                    if dfs(nei,neicolor)==False:
                        return False

            return True
            
        for i in range(1,n+1):
            if color[i]==-1:
                if dfs(i,0)==False:
                    return False

        return True

