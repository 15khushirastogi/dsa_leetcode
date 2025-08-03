class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        d={}
        for i in range(n):
            for j in range(n):
                value=grid[i][j]
                if value not in d:
                    d[value]=1
                else:
                    d[value]+=1
        repeated=-1
        for key in d:
            if d[key]==2:
                repeated=key
        missing=-1
        for i in range(1,n*n+1):
            if i not in d:
                missing=i

        return [repeated,missing]