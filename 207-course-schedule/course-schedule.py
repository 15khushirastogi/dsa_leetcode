class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        return len(topo)==n
            