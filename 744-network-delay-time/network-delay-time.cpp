class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adj(n + 1); 
        for (auto& it : times) {
            adj[it[0]].push_back({it[1], it[2]});
        }

        vector<int> min_time(n + 1, 1e9);
        min_time[k] = 0;

        queue<pair<int,int>>pq;
        pq.push({0, k});

        while (!pq.empty()) {
            int time = pq.front().first;
            int node = pq.front().second;
            pq.pop();

            for (auto& it : adj[node]) {
                int newNode = it.first;
                int newTime = it.second;

                if (time + newTime < min_time[newNode]) {
                    min_time[newNode] = time + newTime;
                    pq.push({min_time[newNode], newNode});
                }
            }
        }

        int ans = *max_element(min_time.begin() + 1, min_time.end());
        return (ans == 1e9) ? -1 : ans;
    }
};
