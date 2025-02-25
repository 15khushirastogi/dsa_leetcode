class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<vector<int>> adj(n);
        
        for(auto &it : edges){
            adj[it[0]].push_back(it[1]);
            adj[it[1]].push_back(it[0]);
        }

        queue<int> q;
        vector<bool> visited(n, false); 
        
        q.push(source);
        visited[source] = true;

        while (!q.empty()) {
            int node = q.front();
            q.pop();

            if (node == destination) return true; 
            
            for (auto nextNode : adj[node]) {
                if (!visited[nextNode]) { 
                    visited[nextNode] = true;
                    q.push(nextNode);
                }
            }
        }
        
        return false; 
    }
};
