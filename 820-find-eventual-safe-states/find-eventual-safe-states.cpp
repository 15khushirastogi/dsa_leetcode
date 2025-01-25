class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int v=graph.size();
        vector<vector<int>>adjrev(v);
        for(int i=0;i<v;i++){
            for(auto it:graph[i]){
                adjrev[it].push_back(i);
            }
        }
        vector<int>indegree(v,0);
        for(int i=0;i<v;i++){
            for(auto it:adjrev[i]){
                indegree[it]++;
            }
        }
        queue<int>q;
        vector<int>ans;
        for(int i=0;i<v;i++){
            if(indegree[i]==0){
                q.push(i);
            }
        }
        while(!q.empty()){
            int node=q.front();
            q.pop();
            ans.push_back(node);

            for(auto it:adjrev[node]){
                indegree[it]--;
                if(indegree[it]==0){
                    q.push(it);
                }
            }
        }
        sort(ans.begin(),ans.end());
        return ans;
    }
};