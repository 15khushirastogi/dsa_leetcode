class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n=numCourses
        adjList=[[] for _ in range(n)]
        for course in prerequisites:
            adjList[course[0]].append(course[1])
        topo=[]
        indegree=[0]*n
        q=deque()
        for course in adjList:
            for adj in course:
                indegree[adj]+=1
        
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        while q:
            course=q.popleft()
            topo.append(course)
            for adj in adjList[course]:
                indegree[adj]-=1
                if(indegree[adj]==0):
                    q.append(adj)

        if len(topo)==n:
            return topo[::-1]
        return []
            