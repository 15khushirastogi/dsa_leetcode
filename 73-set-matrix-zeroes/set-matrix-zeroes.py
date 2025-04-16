class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        q=deque()
        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==0):
                    q.append([i,j])
        while q:
            row,col=q.popleft()

            for i in range(m):
                matrix[row][i]=0
            for j in range(n):
                matrix[j][col]=0


        

        