class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()  # row,col,time
        maxtime = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j, 0])

        while q:
            row, col, time = q.popleft()
            maxtime = max(maxtime, time)
            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]
            for i in range(4):
                newrow = row + dr[i]
                newcol = col + dc[i]

                # check boundary conditions
                if (
                    newrow >= 0
                    and newcol >= 0
                    and newrow < m
                    and newcol < n
                    and grid[newrow][newcol] == 1
                    and grid[newrow][newcol] != 2
                ):
                    grid[newrow][newcol] = 2
                    q.append([newrow, newcol, time + 1])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return maxtime
