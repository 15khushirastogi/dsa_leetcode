class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>>adj(numCourses);
        for(int i=0;i<prerequisites.size();i++){
            int course=prerequisites[i][0];
            int depends=prerequisites[i][1];
            adj[course].push_back(depends);
        }
        vector<int>topo;
        queue<int>q;
        vector<int>indegree(numCourses,0);
        for(int i=0;i<prerequisites.size();i++){
            int in=prerequisites[i][1];
            indegree[in]++;
        }
        for(int i=0;i<indegree.size();i++){
            if(indegree[i]==0){
                q.push(i);
            }
        }
        while(!q.empty()){
            int node=q.front();
            q.pop();
            topo.push_back(node);

            for(auto it:adj[node]){
                indegree[it]--;
                if(indegree[it]==0){
                    q.push(it);
                }
            }
        }
        if(topo.size()<numCourses){
            return false;
        }
        return true;
    }
};