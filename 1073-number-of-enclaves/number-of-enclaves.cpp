class Solution {
public:
    void dfs(int row, int col, vector<vector<int>>& grid, int drow[], int dcol[]) {
        int m = grid.size();
        int n = grid[0].size();
        grid[row][col] = -1; 
        for (int i = 0; i < 4; i++) {
            int nrow = row + drow[i];
            int ncol = col + dcol[i];
            if (nrow >= 0 && nrow < m && ncol >= 0 && ncol < n && grid[nrow][ncol] == 1) {
                dfs(nrow, ncol, grid, drow, dcol);
            }
        }
    }

    int numEnclaves(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int drow[] = {-1, 0, +1, 0};
        int dcol[] = {0, +1, 0, -1};

        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 1) dfs(i, 0, grid, drow, dcol);       
            if (grid[i][n-1] == 1) dfs(i, n-1, grid, drow, dcol);   
        }
        for (int i = 0; i < n; i++) {
            if (grid[0][i] == 1) dfs(0, i, grid, drow, dcol);       
            if (grid[m-1][i] == 1) dfs(m-1, i, grid, drow, dcol);   
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    count++;
                }
            }
        }
        return count;
    }
};
