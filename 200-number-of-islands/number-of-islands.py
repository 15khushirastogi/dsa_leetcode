from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[0] * n for _ in range(m)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            vis[r][c] = 1

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and vis[nr][nc] == 0 and grid[nr][nc] == "1":
                        vis[nr][nc] = 1
                        q.append((nr, nc))

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and vis[i][j] == 0:
                    bfs(i, j)
                    count += 1

        return count
