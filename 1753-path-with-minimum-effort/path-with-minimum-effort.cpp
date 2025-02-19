class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int row = heights.size();
        int col = heights[0].size();

        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<>> pq;
        vector<vector<int>> dist(row, vector<int>(col, 1e9));
        dist[0][0] = 0;
        pq.push({0, {0, 0}});

        int dr[] = {-1, 0, 1, 0};
        int dc[] = {0, 1, 0, -1};

        while (!pq.empty()) {
            auto it = pq.top();
            pq.pop();
            
            int diff = it.first;
            int r = it.second.first;
            int c = it.second.second;

            if (r == row - 1 && c == col - 1) return diff;

            for (int i = 0; i < 4; i++) {
                int newr = r + dr[i];
                int newc = c + dc[i];

                if (newr >= 0 && newr < row && newc >= 0 && newc < col) {
                    int newdiff = abs(heights[newr][newc] - heights[r][c]);
                    int maxEffort = max(newdiff, diff);

                    if (maxEffort < dist[newr][newc]) {
                        dist[newr][newc] = maxEffort;
                        pq.push({maxEffort, {newr, newc}});
                    }
                }
            }
        }
        return 0;
    }
};
