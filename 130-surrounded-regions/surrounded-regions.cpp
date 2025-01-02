class Solution {
    void dfs(int row, int col, vector<vector<char>>& board, int drow[], int dcol[]) {
        int m = board.size();
        int n = board[0].size();
        board[row][col] = '#'; 
        for (int i = 0; i < 4; i++) {
            int nrow = row + drow[i];
            int ncol = col + dcol[i];
            if (nrow >= 0 && nrow < m && ncol >= 0 && ncol < n && board[nrow][ncol] == 'O') {
                dfs(nrow, ncol, board, drow, dcol);
            }
        }
    }

public:
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        int n = board[0].size();
        int drow[] = {-1, 0, +1, 0};
        int dcol[] = {0, +1, 0, -1};

        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') dfs(i, 0, board, drow, dcol);       
            if (board[i][n-1] == 'O') dfs(i, n-1, board, drow, dcol);   
        }
        for (int i = 0; i < n; i++) {
            if (board[0][i] == 'O') dfs(0, i, board, drow, dcol);      
            if (board[m-1][i] == 'O') dfs(m-1, i, board, drow, dcol);   
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                if (board[i][j] == '#') board[i][j] = 'O';
            }
        }
    }
};
