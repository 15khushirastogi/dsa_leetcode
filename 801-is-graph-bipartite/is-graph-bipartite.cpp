class Solution {
public:
    bool dfs(int curr, vector<int>& color, int currcolor, vector<vector<int>>& graph){
        color[curr]=currcolor;
        for(int nei:graph[curr]){
            if(color[nei]==currcolor){
                return false;
            }
            if(color[nei]==-1){
                int neicolor=1-currcolor;
                if(dfs(nei,color,neicolor,graph)==false){
                    return false;
                }
            }
        }
        return true;
    }
    bool isBipartite(vector<vector<int>>& graph) {
        int v=graph.size();
        vector<int>color(v,-1);
        for(int i=0;i<v;i++){
            if(color[i]==-1){
                if(dfs(i,color,0,graph)==false){
                    return false;
                }
            }
            
        }
        return true;
    }
};