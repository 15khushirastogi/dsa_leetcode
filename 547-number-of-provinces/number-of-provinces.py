class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        count=0
        vis=set()
        for i in range(n):
            if i not in vis:
                count+=1
                queue=deque([i])
                vis.add(i)
                while queue:
                    city=queue.pop()
                    for nei in range(n):
                        if isConnected[city][nei]==1 and nei not in vis:
                            vis.add(nei)
                            queue.append(nei)


        return count