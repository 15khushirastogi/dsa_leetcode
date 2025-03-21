class Solution {
private:
    void dfs(int src, int dest, vector<vector<int>>& graph, vector<int>& path, vector<vector<int>>& ans) {
        path.push_back(src);

        if (src == dest) {
            ans.push_back(path);
        } 
        else {
            
            for (int neighbor : graph[src]) {
                dfs(neighbor, dest, graph, path, ans);
            }
        }

        path.pop_back();
    }

public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> ans;
        vector<int> path;
        int n = graph.size();
        int src = 0, dest = n - 1;

        dfs(src, dest, graph, path, ans);
        return ans;
    }
};
